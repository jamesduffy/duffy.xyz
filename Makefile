
build: clean
	hugo

clean:
	rm -r public/

run:
	hugo --buildDrafts --buildFuture --watch serve

run-live:
	hugo --watch serve

deploy: build
	rsync -vr ./public/ duffyxyz:/var/www/duffy.xyz --delete
