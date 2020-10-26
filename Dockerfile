FROM python:3.8

RUN pip install Flask gunicorn

COPY src/ /app
WORKDIR /app

RUN pip install -r requirement.txt

ENV PORT 8080
CMD exec ls
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app