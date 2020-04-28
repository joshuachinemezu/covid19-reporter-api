
build:
	docker build -t covid-reporter-api:latest .

run:
	docker run  -p 5000:5000 covid-reporter-api

ssh:
	docker run --rm -it --entrypoint /bin/sh covid-reporter-api