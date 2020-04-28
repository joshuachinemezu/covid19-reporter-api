appname=covid19-reporter-api

test:
	python3 -m pytest

launch:
	gunicorn app:server
