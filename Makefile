# Formatting and help functionality for this file copied from the c2fo/atlas-docker project.
# ==============================
# HELP
# ==============================

.DEFAULT_GOAL := help

help:
	@printf "USAGE:\n";
	@printf "  \033[36mmake <target>\033[0m"
	@echo ""
	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf "  \033[36m%-20s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-\_0-9.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "  \033[36m%-20s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = helpMessage"\n"substr($$0, 3); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n"helpMessage"\n" \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

# ==============================
# TARGETS
# ==============================

##COMMANDS:

## Create a Python virtual environment in the root directory
create-env:
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

## Run tests
test:
	./.venv/bin/python -m unittest discover -s tests -p "*_test.py"

## Check format using Black
check-format:
	black . --check

## Format code using Black
format:
	black .