FROM python:3.8-slim-buster

RUN pip3 install Flask==2.3.2

COPY . .

EXPOSE 4000

CMD ["python3", "app.py"]
