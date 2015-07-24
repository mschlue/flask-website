FROM ubuntu:trusty
MAINTAINER Matthew Schlue isuschlue@gmail.com

RUN apt-get update && apt-get install -y \
    python-pip \
    python-dev

ADD . /flask-website

RUN pip install pip==6.0.0
RUN pip install -r /flask-website/requirements.txt

EXPOSE 5000
CMD ["python", "/flask-website/main.py"]
