FROM python:3.9-slim-buster

RUN pip install --no-cache-dir faker numpy

WORKDIR /app

COPY fake.py /app/fake.py

CMD [ "python", "fake.py", "loop" ]