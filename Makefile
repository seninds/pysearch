all: check

check:
	@mypy --strict $$(find . -type f -name "*.py")