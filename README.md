# Django-Bootstrap

Template for starting a containerized Django app running on docker-compose

# Useful Commands
## Create superuser (Django Admin)
    docker-compose exec web python manage.py createsuperuser
  
## Dev. Deployment
    docker-compose down -v
    docker-compose build
    docker-compose up -d

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
This Template was based on [this](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) guide
Custom SystemUser was created using [this](https://testdriven.io/blog/django-custom-user-model/) guide
Bootstrap4 was added by following [this](https://blog.nubecolectiva.com/como-integrar-django-y-bootstrap-4/) guide
[Bootstrap 4 Docs](https://getbootstrap.com/docs/4.0/components)

