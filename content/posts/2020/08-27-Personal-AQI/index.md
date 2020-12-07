---
title: "Personal AQI Service"
date: 2020-08-27T08:00:00Z
tags:
    - python
    - grafana
---

Every year in California the fire season feels like it gets longer and more devastating. This year with everything else going on it feels especially bad. This year I took the time to build a ingestion script of [PurpleAir](https://purpleair.com/) sensor data, graph it with Grafana and send alerts when the air near my apartment reaches >50 AQI.

To build this I used PurpleAir's API to pull sensor data every ~5 minutes and write it to MySQL. I then setup Grafana and created a dashboard with a map of sensors and points of interest. Grafana also manages sending a push notification using Pushover.net when AQI is above 50 for 10 minutes.

MySQL and Grafana are both running in containers on my Synology NAS with external volume storage. 

I wrote a Python script that runs on my Intel NUC that gets triggered by a CRONJOB every five minutes. This script does the following steps:

1. Pull JSON data from PurpleAir
2. Filter out any sensor that does not meet the below requirements:
   - Not located "outside"
   - Not reported in the last 5 minutes
   - Not within specific Longitude and Latitude
3. Take the raw PM 2.5 Value and convert to US AQI
4. Insert all data into database

# MySQL Table
```sql
CREATE TABLE `sensor_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `purpleair_id` int DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `time` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  `longitude` decimal(11,8) DEFAULT NULL,
  `geohash` varchar(12) DEFAULT NULL,
  `pm2_5` decimal(8,2) DEFAULT NULL,
  `aqi` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `purpleair_id` (`purpleair_id`),
  KEY `time` (`time`),
  KEY `idx_sensor_data_aqi` (`aqi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

# Ingestion Script
```python
import requests
import time

import pymysql
import pymysql.cursors

from json.decoder import JSONDecodeError

from retrying import retry

# Connect to the database
connection = pymysql.connect(
    host='',
    user='',
    password='',
    db='',
    charset='utf8')


def aqi_from_pm(pm):
    if pm > 350.5:
        return calculate_aqi(pm, 500, 401, 500, 350.5)
    elif pm > 250.5:
        return calculate_aqi(pm, 400, 301, 350.4, 250.5)
    elif pm > 150.5:
        return calculate_aqi(pm, 300, 201, 250.4, 150.5)
    elif pm > 55.5:
        return calculate_aqi(pm, 200, 151, 150.4, 55.5)
    elif pm > 35.5:
        return calculate_aqi(pm, 150, 101, 55.4, 35.5)
    elif pm > 12.1:
        return calculate_aqi(pm, 100, 51, 35.4, 12.1)
    elif pm >= 0:
        return calculate_aqi(pm, 50, 0, 12, 0)
    else:
        return False


def calculate_aqi(Cp, Ih, Il, BPh, BPl):
    a = Ih - Il
    b = BPh - BPl
    c = Cp - BPl
    return round(((a/b) * c + Il))


@retry(wait_fixed=30000, stop_max_attempt_number=3)
def fetch_results():
    purpleair = requests.get("https://www.purpleair.com/json")
    return purpleair.json()['results']

purpleair_results = fetch_results()

sql = "INSERT INTO `sensor_data` (`purpleair_id`, `time`, `name`, `latitude`, `longitude`, `pm2_5`, `aqi`) VALUES (%s, %s, %s, %s, %s, %s, %s)"

data = []
for measurement in purpleair_results:
    is_outside = 'DEVICE_LOCATIONTYPE' in measurement and measurement['DEVICE_LOCATIONTYPE'] == 'outside'
    is_recent = 'AGE' in measurement and measurement['AGE'] <= 300
    is_valid = 'ID' in measurement and 'Label' in measurement and 'Lat' in measurement and 'Lon' in measurement and 'PM2_5Value' in measurement

    if is_outside and is_recent and is_valid:
        # Include California and some of the surrounding area
        is_longitude =  -125.22216797 < measurement['Lon'] < -113.26904297
        is_latitude = 32.17561248 < measurement['Lat'] < 42.16340342

        if is_longitude and is_latitude:
            raw_pm = measurement['PM2_5Value']
            pm2_5 = float(raw_pm) if '.' in raw_pm else False

            if pm2_5:
                data.append([
                    measurement['ID'],
                    measurement['LastSeen'],
                    measurement['Label'].strip(),
                    measurement['Lat'],
                    measurement['Lon'],
                    pm2_5,
                    aqi_from_pm(pm2_5)
                ])

cursor = connection.cursor()

for sensor in data:
    print(sensor)
    cursor.execute(sql, sensor)

connection.commit()

connection.close()
```
