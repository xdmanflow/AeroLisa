.PHONY: install test lint format up down clean

install:
	pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

up:
	docker compose up -d

down:
	docker compose down

clean:
	rm -rf .pytest_cache .ruff_cache build dist *.egg-info
