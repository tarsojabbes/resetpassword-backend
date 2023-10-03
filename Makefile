SHELL := /bin/bash
DOCKER_IMAGE?=reset-senhas-backend
CONTAINER_NAME?=reset-senhas-backend

build:
	docker build -t ${DOCKER_IMAGE} .

run:
	docker run --env-file .env --rm -p 5000:5000 ${DOCKER_IMAGE}

rund:
	docker run --env-file .env -d --rm -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}

stop:
	docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}
