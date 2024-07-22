FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y netcat-traditional
RUN pip install --upgrade pip

RUN pip install "poetry"
COPY pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


COPY runserver.sh /
RUN chmod +x /runserver.sh

EXPOSE 8000

COPY . /code/

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
