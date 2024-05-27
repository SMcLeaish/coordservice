FROM python:3.11-slim as builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY coordextract coordextract
COPY tests tests

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/.venv .venv

COPY coordextract coordextract

ENV PATH="/app/.venv/bin:$PATH"

CMD ["poetry", "run", "uvicorn", "coordextract:app", "--host", "0.0.0.0", "--port", "8000"]

