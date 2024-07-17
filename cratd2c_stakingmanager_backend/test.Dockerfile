FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip==20.2.4
RUN apt-get update && apt-get install -y netcat
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY ./test-start /test-start
RUN chmod +x /test-start

ENTRYPOINT ["/entrypoint.sh"]
