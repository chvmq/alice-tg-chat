FROM python:3.8.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv

COPY . /app/

RUN pipenv install --system --ignore-pipfile

RUN ls -all

CMD [ "python3", "-m", "src.main" ]
