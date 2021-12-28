SHELL := /bin/bash

include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: ## Testing the app
	@poetry run python runtests.py

.PHONY: install
install: ## Install the env
	@poetry install
	@poetry run pre-commit install
	@poetry run pre-commit autoupdate

.PHONY: update
update: ## Update the dependency project
	@poetry update

.PHONY: docs
docs:  ## Previewing as you write documentation
	@poetry run mkdocs build --clean

.PHONY: html
html: docs## Serve the docs
	@poetry run mkdocs serve

.PHONY: migrate
migrate:  ## Make migrations
	@poetry run python manage.py makemigrations

.PHONY: tox
tox: ## Launch tox test
	@poetry run tox

.PHONY: clean
clean: ## Clean the directory from test stuffs
	@rm -f .coverage.*
	@rm -fr .xmlcoverage
	@rm -fr .tox
	@rm -fr dist

prepublish: test tox clean ## Code for the prepublish

publish: prepublish ## Testing and publish the paackage
	@poetry publish --build
