FROM python:3.8.3-alpine

WORKDIR /code
ADD ./backend/requirements.txt /code/backend/


RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r backend/requirements.txt

ADD ./docker /code/docker
ADD ./backend /code/backend