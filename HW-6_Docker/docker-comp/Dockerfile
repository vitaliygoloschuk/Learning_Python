FROM python:latest

WORKDIR /usr/app/src
RUN apt-get update && apt-get install -y iputils-ping
COPY main.py  ./

CMD ["python","main.py"]