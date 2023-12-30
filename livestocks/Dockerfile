# base image
FROM python:3.10.12

# setup env vars
ENV DockerHome = /home/app

# set work dir
RUN mkdir -p $DockerHome

# where your code lives
WORKDIR $DockerHome

# set enviromnment vars ????
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home dir
COPY . $DockerHome

# run this compand to install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# start server
CMD python manage.py runserver
