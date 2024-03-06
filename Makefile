.PHONY: test test-debug up down clean coordservice build

test:
	docker-compose run --rm app sh -c "\
		poetry install && \
		poetry run isort . --check && \
		poetry run black . --check && \
		poetry run mypy . && \
		poetry run pytest"

test-debug:
	docker-compose run --rm app sh -c "\
		poetry install && \
		poetry run pytest -s"

build:	
	docker build -t smcleaish/coordservice .
up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down --volumes &&\
		docker rmi smcleaish/coordservice

coordservice: build up

