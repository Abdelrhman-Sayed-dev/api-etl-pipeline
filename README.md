# API ETL Pipeline

A Python ETL pipeline that extracts data from a REST API, transforms and cleans the data using Pandas, validates it, and loads it into PostgreSQL.

## Architecture

```text
REST API
   ↓
Extract
   ↓
Transform
   ↓
Clean & Validate
   ↓
PostgreSQL
```

## Tech Stack

* Python
* Pandas
* Requests
* PostgreSQL
* Psycopg
* Docker

## Features

* REST API data extraction
* JSON data normalization
* Data transformation and cleaning
* Data validation
* PostgreSQL loading
* Incremental loading
* Duplicate prevention
* Logging
* Dockerization

## Run

```bash
python src/main.py
```

Or with Docker:

```bash
docker build -t api-etl-project .
docker run --rm api-etl-project
```
