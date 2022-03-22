FROM ubuntu:21.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y upgrade
FROM python:3.8-alpine
RUN apt-get -y install git
RUN apt-get -y update
RUN apt-get -y upgrade
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["app.py" ]