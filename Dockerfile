FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

EXPOSE 80

ENV NAME World

CMD ["python", "main.py"]
