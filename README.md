# django-starter-template

## Installation

1. Create a new directory for your project and move into it. You should replace `my-project` with the name of your project.
```bash
mkdir my-project && cd $_
```

2. Next, create a new virtual environment and activate it.
```bash
python3 -m venv venv && source venv/bin/activate
```

3. Then install django
```bash
pip3 install django
```

4. Finally, start the django project from a template using 
the git repository. Replace `my-project` with the name of your project.
```bash
django-admin startproject --template=https://github.com/colinmipapi/django-starter-template/archive/main.zip --name=Dockerfile --extension=py,yml,json,env my_project .
```

5. Setup the example.env file as your .env file. The default variables have been configured, but there are additional variables that can be set to help customize your project. 
```bash
mv example.env .env
```


6. Now you are able to setup Docker
```bash
docker-compose up --build
```

<p></p>

## Configuration

### Environment Variables

```
# GENERAL
# ------------------------------------------------------------------------------

DJANGO_DEBUG=TRUE
SECRET_KEY=-68!#6l7u9uavsq+pl%v0b%2rgi(0y5c!fl8x2xci9t8banjbk3
DJANGO_SETTINGS_MODULE={{ project_name }}.settings.local
#DJANGO_ALLOWED_HOSTS=


# PROJECT DETAILS
# ------------------------------------------------------------------------------

# Enter the human readable name of your project this value is used in the templates
#PROJECT_VERBOSE_NAME=

# The URL for your logo. Used in templates
#PROJECT_LOGO_URL=

# The phone number for your project. Used in the privacy policy and terms & conditions templates
#PROJECT_PHONE_NUMBER=


# DATABASES
# ------------------------------------------------------------------------------
DATABASE_URL=postgres://postgres:postgres@localhost:5432/{{ project_name }}-db


# SECURITY
# ------------------------------------------------------------------------------

#DJANGO_SESSION_COOKIE_NAME=


# STATIC
# ------------------------------------------------------------------------------

#DJANGO_STATICFILES_STORAGE=
#DJANGO_STATIC_ROOT=
#DJANGO_STATIC_URL=


# MEDIA
# ------------------------------------------------------------------------------

#DJANGO_MEDIA_ROOT=
#DJANGO_MEDIA_URL=


# EMAIL
# ------------------------------------------------------------------------------

#DJANGO_DEFAULT_FROM_EMAIL=
#DJANGO_SERVER_EMAIL=
#DJANGO_EMAIL_SUBJECT_PREFIX=
#DJANGO_EMAIL_BACKEND=


# ADMIN
# ------------------------------------------------------------------------------

#DJANGO_ADMIN_URL=


# DJANGO ALLAUTH
# ------------------------------------------------------------------------------

#GOOGLE_CLIENT_ID=
#GOOGLE_CLIENT_SECRET=


# CELERY
# ------------------------------------------------------------------------------

#DJANGO_CELERY_BROKER_URL=
#DJANGO_CELERY_RESULT_BACKEND=


# DJANGO ELASTICSEARCH DSl
# ------------------------------------------------------------------------------

#DJANGO_ELASTICSEARCH_HOST=
```
