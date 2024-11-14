FROM python:3.12.7 AS builder
WORKDIR /code
RUN pip install poetry==1.8.4
ENV POETRY_VIRTUALENVS_CREATE=true \
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  POETRY_CACHE_DIR=/tmp/poetry_cache
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root --only main

FROM python:3.12.7 AS runtime
WORKDIR /code
ENV PATH="/code/.venv/bin:${PATH}" \
  PYTHONUNBUFFERED=1
COPY --from=builder /code/.venv /code/.venv
RUN apt-get update && apt-get install -y --no-install-recommends netcat-traditional \
  && rm -rf /var/lib/apt/lists/*
COPY runserver.sh /
COPY . /code/
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
