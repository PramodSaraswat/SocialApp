web: flask db upgrade; flask translate compile; gunicorn main:app
worker: rq worker -u $REDIS_URL microblog-tasks