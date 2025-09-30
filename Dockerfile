FROM python:3.12-slim

LABEL org.opencontainers.image.source=https://github.com/lucas-lm/thunderchef-api

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
# c++ compiles (required for psycopg2 - python's postgres library)
RUN apt update && apt install -y build-essential libpq-dev python3-dev
# project dependencies
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"]
