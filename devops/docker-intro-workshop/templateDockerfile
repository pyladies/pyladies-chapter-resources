FROM python:3.7

MAINTAINER Pyladies Workshop

WORKDIR /myapp

COPY app/ /myapp/app
COPY requirements.txt /myapp

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]

