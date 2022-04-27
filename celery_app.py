import os

from celery import Celery
from kombu import Exchange, Queue

import celeryconfig


celery_app = Celery("worker")

celery_app.config_from_object(celeryconfig)

tasks = []
queues = []
tasks_path = f"{os.getcwd()}/app/tasks"

files = os.listdir(tasks_path)
for task in files:
    if not task.startswith("_") and task.endswith(".py"):
        task = task.split(".")[0]
        tasks.append(f"app.tasks.{task}")

        queues.append(
            Queue(
                task,
                Exchange(task, type="direct"),
                routing_key=f"app.task.{task}",
                queue_arguments={"x-max-priority": 255},
            ),
        )
celery_app.conf.task_queues = queues
celery_app.autodiscover_tasks(tasks)
