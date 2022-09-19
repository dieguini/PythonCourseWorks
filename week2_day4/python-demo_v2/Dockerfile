# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /python-demo

COPY ./requirements.txt /python-demo/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /python-demo/requirements.txt

COPY ./code /python-demo/

CMD [ "python3", "./app.py" ]