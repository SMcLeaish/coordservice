FROM python:3.11-slim AS builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY coordextract ./coordextract

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev

FROM docker:latest

COPY --from=builder /app /app

WORKDIR /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "coordextract:app", "--host", "0.0.0.0", "--port", "8000"]

