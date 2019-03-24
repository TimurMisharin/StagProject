# StagProject


# to create project
	django-admin startproject <projectname>
# to run server
	python manage.py runserver (localhost:8000)
# to create app
	python manage.py startapp <appname>
# create migrations (need to install Pillow for ImageField in models)
	python manage.py makemigrations
# run migrations
	python manage.py migrate