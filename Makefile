SHELL := /bin/bash
DOCKER_IMAGE?=reset-senhas-backend

build:
	docker build -t ${DOCKER_IMAGE} .

run:
	docker run --rm --network host ${DOCKER_IMAGE}

rund:
	docker run -d --network host ${DOCKER_IMAGE}
