.PHONY: setup clean build test install

# Variables
POETRY = poetry

# Setup Poetry environment and install dependencies
setup:
	$(POETRY) install

# Build the package
build: setup
	$(POETRY) build

# Clean up build artifacts and Poetry environment
clean:
	rm -rf dist/
	rm -rf *.egg-info/
	$(POETRY) env remove --all

# Run tests
test: setup
	$(POETRY) run pytest tests/

# Install the package in development mode
install: setup
	$(POETRY) install

# Show help
help:
	@echo "Available commands:"
	@echo "  make setup      - Install dependencies using Poetry"
	@echo "  make build      - Build the package using Poetry"
	@echo "  make clean      - Remove build artifacts and Poetry environment"
	@echo "  make test       - Run tests"
	@echo "  make install    - Install package in development mode"
	@echo "  make help       - Show this help message" 