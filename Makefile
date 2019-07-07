.PHONY: docker-build docker-up docker-stop docker-enter pip python install

PYTHON = python3
PIP = python3 -m pip
APT = apt-get

docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-stop:
	docker-compose stop

docker-enter:
	docker exec -it adamzelycz-ddns-updater bash

pip:
	$(PIP) install -r $(REQUIREMENTS)

python:
	${APT} update && ${APT} -y install ${PYTHON} ${PYTHON}-pip; \
	$(PIP) install --upgrade pip > /dev/null

install: python pip
