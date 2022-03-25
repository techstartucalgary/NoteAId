# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN [ "python", "-c", "import nltk; nltk.download('punkt'); nltk.download('stopwords');" ]
COPY . .
ENV GOOGLE_APPLICATION_CREDENTIALS="creds.json"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
