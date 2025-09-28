# Thunderchef

## Developer Guide

Clone the repository:
```sh
git clone https://github.com/lucas-lm/thunderchef-api
```

Install uv (needs `curl`):
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install commitizen (required for bump process):
```sh
# Install commitizen
uv tool install commitizen

# Keep it updated
uv tool upgrade commitizen
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

Commiting staged changes (after `git add`):
```sh
cz commit
```

Bumping a new version (use `--dry-run` flag if you want to make sure about the changes):
```sh
cz bump
```

Send changes with tags to remote repository:
```sh
git push --tags
```

New tags following the format `v$version` (SemVer) triggers the pipeline to push the images to GitHub Packages.