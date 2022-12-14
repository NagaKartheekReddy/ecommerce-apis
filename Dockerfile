# base image
FROM python:3.8

# setup environment variable
ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir -p $DockerHOME

# work directory where our whole project located
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to our docker home directory.
COPY . $DockerHOME

# run command to install all dependencies
RUN pip install -r requirements.txt
