
build: clean
	python manage.py freeze

clean:
	rm -r build/

run:
	python manage.py runserver

deploy: build
	rsync -vr ./build/ duffyxyz:/webapps/duffy.xyz --delete
