FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


RUN mkdir /app
WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5050

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]