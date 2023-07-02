SHELL := /bin/bash
DOCKER_IMAGE?=reset-senhas-backend

build:
	docker build -t ${DOCKER_IMAGE} .

run:
	docker run --env-file .env --rm --network host ${DOCKER_IMAGE}

rund:
	docker run --env-file .env -d --network host ${DOCKER_IMAGE}
