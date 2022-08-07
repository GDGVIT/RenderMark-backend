CELERY_BROKER_URL = "redis://localhost:6379/0"
result_backend = "redis://localhost:6379/0"
imports = ("tasks.tasks",)
