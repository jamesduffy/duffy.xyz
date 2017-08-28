
default:
	python manage.py runserver

deploy:
	rm -r build/
	python manage.py freeze
	rsync -vr ./build/ duffyxyz:/webapps/duffy.xyz
