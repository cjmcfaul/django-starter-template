# django-starter-template

## Prerequisites

You need to having the following programs setup on your system before 
trying to install/run this project.

1. Python3 
2. Docker
3. Git 

## Installation

1. Create a new directory for your project and move into it. You should 
replace `my-project` with the name of your project.
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

5. Setup the example.env file as your .env file. The default variables 
have been configured, but there are additional variables that can be 
set to help customize your project. 
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
The sections of the example.env file match up with the sections of the 
settings files where the environment variable is used.

#### General
```
DJANGO_DEBUG=TRUE
SECRET_KEY=-68!#6l7u9uavsq+pl%v0b%2rgi(0y5c!fl8x2xci9t8banjbk3
DJANGO_SETTINGS_MODULE={{ project_name }}.settings.local

DJANGO_ALLOWED_HOSTS=
```

#### Project Details
```
# Enter the human readable name of your project this value is used in the templates
PROJECT_VERBOSE_NAME=

# The URL for your logo. Used in templates
PROJECT_LOGO_URL=

# The phone number for your project. Used in the privacy policy and terms & conditions templates
PROJECT_PHONE_NUMBER=
```

#### Databases
```
DATABASE_URL=postgres://postgres:postgres@localhost:5432/{{ project_name }}-db
```

#### Security
```
DJANGO_SESSION_COOKIE_NAME=
```

#### Static
```
DJANGO_STATICFILES_STORAGE=
DJANGO_STATIC_ROOT=
DJANGO_STATIC_URL=
```

#### Media
```
DJANGO_MEDIA_ROOT=
DJANGO_MEDIA_URL=
```

#### Email
```
DJANGO_DEFAULT_FROM_EMAIL=
DJANGO_SERVER_EMAIL=
DJANGO_EMAIL_SUBJECT_PREFIX=
DJANGO_EMAIL_BACKEND=
```

#### Admin
```
DJANGO_ADMIN_URL=
```

#### Django Allauth
```
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
```
#### CELERY
```
DJANGO_CELERY_BROKER_URL=
DJANGO_CELERY_RESULT_BACKEND=
```

#### ELASTICSEARCH
```
DJANGO_ELASTICSEARCH_HOST=
```


## Coming Soon!

I'm going to try and add additional features and functionality to the 
project over the coming weeks and months. Feel free to reach out if 
there's anything else you think should be added to the list.

- [ ] Base Templates
- [ ] Index / Home Page Template
- [ ] About Page Template
- [ ] Contact Us Template & Form
- [ ] User Settings Template & Form
- [ ] Custom django-allauth templates