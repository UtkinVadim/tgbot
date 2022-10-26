run_bot:
	python manage.py start_bot

run_web:
	python manage.py runserver

run docker:
	docker-compose up --build -d tgbot