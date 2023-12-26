format:
	@rye run ruff check . --fix --show-fixes
	@rye run black .
	@rye run mypy .
