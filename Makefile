.PHONY=help

run-api:
	@python app.py

run-worker:
	@celery -A celery_app worker -l info

run-cron:
	@celery -A celery_app beat -l info
