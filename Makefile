
build: clean
	hugo

clean:
	rm -r public/

run:
	hugo --buildDrafts --watch serve

deploy: build
	rsync -vr ./public/ duffyxyz:/var/www/duffy.xyz --delete
