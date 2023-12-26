help:
	@cat Makefile | sed '/^$$/d' | sed '/^\t/d' | sed '/:=/d' | sed '/^_/d' | sed 's/:.*#/\t/g' | expand -t 25

install:
	@rye sync

format:
	@rye run ruff check . --fix --show-fixes
	@rye run black .
	@rye run mypy .
