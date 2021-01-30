# Django-Bootstrap [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Template for starting a containerized **Django** app with **Postgres** running on **docker-compose**, Also adding **Gunicorn** (_a production-grade WSGI server_), and **Nginx** (_reverse proxy for Gunicorn to handle client requests as well as serve up static files_) into the mix for production environments.

### Dependencies:
- Python 3.8.3
- Postgres 12.0
- Django 3.0.7
- gunicorn 20.0.4
- psycopg2-binary 2.8.5
- django-bootstrap4

### Quickstart:
    docker-compose build
    docker-compose up -d
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
#### Your App should be up and runnig on http://localhost:8000/ 😀
![app](https://raw.githubusercontent.com/dedarritchon/Django-Bootstrap/0c14a67d70ebffba2998cd31e5dd6c9e7ed9a857/app.png)
# Useful Commands
## Create superuser (Django Admin)
    docker-compose exec web python manage.py createsuperuser

with this user you'll be able to login to the Django /admin page  
## Dev. Deployment
    docker-compose build
    docker-compose up -d (-d for detached)
    docker-compose down
    docker-compose down -v (also removes the volumes along with the containers)
    docker-compose logs -f -t (-f: follow the logs of all running services, -t: adds timestamps to logs)

## DB Related
### Flush
    docker-compose exec web python manage.py flush --no-input
### Migrations
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
### DB shell
    docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

## Prod. Deployment
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

## Create independent image
    docker build -f ./app/Dockerfile -t hello_django:latest ./app
    docker run -d \
        -p 8006:8000 \
        -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" \
        hello_django python /usr/src/app/manage.py runserver 0.0.0.0:8000
      
# Useful Links
This Template was created using [this](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) guide

Custom SystemUser was created using [this](https://testdriven.io/blog/django-custom-user-model/) guide

Bootstrap4 was added by following [this](https://blog.nubecolectiva.com/como-integrar-django-y-bootstrap-4/) guide

[Django Docs](https://docs.djangoproject.com/en/3.1/), [Bootstrap 4 Docs](https://getbootstrap.com/docs/4.0/components)

## Contributing
- **Fork** and **Clone** this repo
- Make a **new branch**
- Make necessary changes and **commit** those changes
- **Push** changes to GitHub
- Submit your changes for review (**Pull Request**)
