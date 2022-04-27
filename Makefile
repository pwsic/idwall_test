.PHONY=help

run-api:
	@python app.py

run-worker:
	@celery -A celery_app worker -l info
