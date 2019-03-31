# Wizard Website

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

### Installation

Wizard site requires [Python](https://www.python.org/) v3+ to run. 

Install the dependencies and devDependencies and start the server.

```sh
...\> pip install Django
...\> pip install Pillow

...\> py manage.py migrate
...\> py manage.py makemigrations posts

...\> py manage.py createsuperuser

...\> py manage.py runserver
```

### Clean Up
This is only used when you want to clean up the entire database, e.g. you're playing with your DB and wants to start implementing real things now.

Dump all data in the DB: ```sh python manage.py flush ```
Reset migrations:
```sh
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```
Discard current schema: ```sh rm db.sqlite3 ```
Run migrations again

Now all things should be reset.