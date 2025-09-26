# Thunderchef

## Development Guide

Clone the repository:
```sh
git clone https://github.com/lucas-lm/thunderchef-api
```

Install uv (needs `curl`):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install dependencies:
```sh
uv install
```

Add environment variables:
```sh
cp .env.example .env  # don't forget to replace the values accordingly in .env file
```

Activate virtual environment:
```sh
source .venv/bin/activate
```

Run development server with hot-reload:
```sh
fastapi dev app/main.py --reload
```

With docker:
```sh
docker compose up -d
```