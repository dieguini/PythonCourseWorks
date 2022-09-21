FROM python:3.9
LABEL version="1.0"

WORKDIR /attendance_app

COPY ./requirements.txt /attendance_app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /attendance_app/requirements.txt

# Copying folders and application files
COPY ./attendace_reports/ /attendance_app/attendace_reports
COPY ./src /attendance_app/src
COPY ./tests /attendance_app/tests
COPY ./README.md .

CMD [ "pip3" , "./src/main.py" ]

## TODO: Teams Attendance docker image definition, it must allow to run src.main.py