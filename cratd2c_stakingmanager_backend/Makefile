.PHONY: test 

init: init-envs pre-commit
init-envs:
	cp env.example .env
	cp config.example.yaml config.yaml

test:
	sudo docker-compose -f test.yml up --build --abort-on-container-exit

build:
	sudo docker-compose up --build -d 

full-migrate: makemigrations migrate
makemigrations:
	sudo docker-compose exec web ./manage.py makemigrations
migrate:
	sudo docker-compose exec web ./manage.py migrate

shell:
	sudo docker-compose exec web ./manage.py shell_plus
collectstatic:
	sudo docker-compose exec web ./manage.py collectstatic
admin:
	sudo docker-compose exec web ./manage.py createsuperuser
web-logs:
	sudo docker-compose logs -f web

pre-commit:
	pip install pre-commit --upgrade
	pre-commit install
