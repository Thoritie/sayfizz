FROM python:3.7

WORKDIR /app

COPY . .

RUN ["pip3", "install", "pipenv"]
RUN ["pipenv", "install"]
CMD pipenv run python app.py
