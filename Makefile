# Default make goal
.DEFAULT_GOAL := help

.PHONY: sync
sync: ## Sync Python dependencies with uv package manager
	@uv sync

.PHONY: run-application
run-application: sync ## Run the Streamlit application
	@uv run streamlit run Z_multichat.py

.PHONY: build
build: ## Tear down local setup
	@docker build -t st_multichat_v

.PHONY: up
up: ## Spin up all local containers in watch mode
	@docker compose -f ./Z_DeployMe/Docker-Compose.yml up -d

.PHONY: down
down: ## Tear down local setup
	@docker compose -f ./Z_DeployMe/Docker-Compose.yml down