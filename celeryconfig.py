from celery.schedules import crontab

broker_transport_options = {
    "queue_order_strategy": "priority",
}

broker_url = "amqp://guest:guest@localhost:5672"

worker_send_task_events = True
task_send_sent_event = True
timezone = "UTC"
task_annotations = {"*": {"default_retry_delay": 5}}

beat_schedule = {
    "run-temporizer-task": {
        "task": "app.tasks.reprocess.reprocess",
        # "schedule": crontab(minute="*/1"),
        "schedule": 10.0,
    },
}
