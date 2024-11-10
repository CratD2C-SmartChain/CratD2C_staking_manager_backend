# cratd2c_stakingManager_backend

- [Getting Started](#getting-started)
- [Project Features](#project-features)
  - [Makefile](#makefile)
  - [Pre Commit](#pre-commit)

## Getting Started

After clone or init git repo you need to call init command.

```
make init
```

After that you need to set environment variables in `.env` and `config.yaml` files.

The next step is to build the project.

```
make build
```

When the web is fully built you can continue to configure the project.

```
make full-migrate   # makemigrations and migrate
make admin          # createsuperuser
make collectstatic  # collectstatic
```

## Project Features

This project is built on DRF and PostgreSQL.

### Makefile

This project uses **Makefile**. List of make commands:

```
make init
make build
make web-logs
make full-migrate   # makemigrations and migrate
make admin          # createsuperuser
make collectstatic  # collectstatic
```

### Pre-Commit

This project uses [pre-commit](https://pre-commit.com/). List of base linters:

- black
- flake8
- isort

### Docs

[Download PDF](cratD2C_stakingManager_backend.pdf)

### SSL Certificate Generation for Redis

Follow these steps to generate SSL certificates for Redis:

1. **Create a directory for certificates**
   First, create a directory to store the certificates and navigate into it:

```bash
mkdir redis_certs
cd redis_certs
```

2. **Generate CA certificate**

```bash
openssl genrsa -out ca.key 2048
```

```bash
openssl req -new -x509 -key ca.key -out ca.crt -days 365
```

3. **Generate a private key for the Redis server**

```bash
openssl genrsa -out redis_server.key 2048
```

4. **Generate a self-signed SSL certificate for the server, valid for 365 days:**

```bash
openssl req -new -x509 -sha256 -key redis_server.key -out redis_server.crt -days 365
```

5. **Create a combined certificate file**

```bash
cat redis_server.crt redis_server.key > redis_server.pem
```
