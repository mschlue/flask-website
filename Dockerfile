FROM ubuntu:xenial
MAINTAINER Matthew Schlue isuschlue@gmail.com

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y \
    python-pip \
    python-dev

ADD . /flask-website

RUN pip install pip==7.1.2
RUN pip install /flask-website/.

EXPOSE 5000
CMD ["webserver"]
