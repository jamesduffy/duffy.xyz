---
title: "Settings up SSL and non SSL Nginx sites to play nice together"
date: 2014-11-15 02:29:00
aliases:
    - /journal/2014/settings-up-ssl-and-non-ssl-nginx-sites-to-play-nice-together/
---

I learned the hard way recently the importance of setting additional Nginx server configurations when hosting both SSL and Non-SSL sites on the same machine.

When I created a new server with an SSL connection and did not set a connection reset for the other sites that were not using SSL I found Google and other search engines were showing the wrong URL in my search results.

<!--more-->

It took almost two weeks for the fix to propagate to all the search engines after I fixed it so don’t make the same mistake I did.

<hr>

Make sure to create Nginx servers for HTTPS and HTTP for each website the machine will be hosting.

I made sure that the default configuration (IP without the domain or unknown server name would just reset the connection and not try to load another site. I also made sure that I forced SSL on sites that had it by redirecting users if they weren&#8217;t using SSL.

On sites that don&#8217;t use SSL I made a server running on SSL with the correct name that would reset the connection. I could possibly redirect the user back to an HTTP connection, but I don&#8217;t think it is necessary and have not tried it myself to make sure that it works.

HTTP Server IP connection reset (444)<br />
HTTPS Server IP connection reset (444)<br />
<span style="text-decoration: underline;">http://example.com</span> redirection to https<br />
<span style="text-decoration: underline;">https://example.com</span> example

<b>/etc/nginx/sites-enabled/default</b>
<pre><code>server {
     listen 80 default;
     return 444;
}

server {
    listen 443 default;
    ssl on;
    ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
    ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
    return 444;
}
</code></pre>

<b>/etc/nginx/sites-enabled/example</b>
<pre><code>server {
    listen  80;
    server_name example.com;
    rewrite ^ https://example.com$request_uri?;
}

server {
    listen  443;
    server_name example.com;
    ssl on;
    ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem;
    ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key;
    keepalive_timeout 60;

    location / {
            proxy_pass http://127.0.0.1:81;
            proxy_set_header        Host    $host;
            proxy_set_header        X-Real-IP      $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
</code></pre>
