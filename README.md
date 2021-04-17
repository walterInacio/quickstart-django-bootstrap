# quickstart-django-bootstrap

This project is a study in django framework, was developer a CRUD using this technology
to understand better how it works.

Project structure:

## Core
In this folder was created forms, models and also setting default of django initializer.
The file `forms.py` contain all forms used in the app, the file `models.py` contain the
model related with the database.

The `urls.py` contain all URL's used in the implementation such as `novoEsporte`, `editEsporte`.
At the `view.py` the user is able to get all the endpoints created during the API.

## Static
Like the says, the static folder have all static libs used in the app, such as bootstrap, fontawesome,
and the stylesheet used to improve layout.

## Migrations
All changes related databases will be reflected as a migration, the migration folder contain all this files
and the user is able to see what was modified.

## Templates
During the development was created files to represent all routes inside the app, the main route have the list of
sports and when the user choose to update and add a new sport the application will change the template when the route
changes.

## Build
After use the project the user one need to start application with two commands
> python manage.py makemigrations
> python manage.py migrate

This commands was create the database and also a table with name `esporte`,
The user can use a software to see all data inserted in the app. The software is `DB Browser for SQLite`,

> Note: The app was created as a single thread, so if the user try to make request in the app and they crash
> the user one needs to close the program and if necessary kill the process to disconnect database...

## Run
To run this project the user needs to complete all build steps and then run the command:
> python manage.py runserver

## Tips
The version python used in this app is the python3 so if the user have a problem with the versions below
try to update.