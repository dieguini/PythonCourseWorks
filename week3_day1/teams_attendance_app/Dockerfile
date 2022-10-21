FROM python:3.9.15-slim
LABEL version="1.0"

WORKDIR /attendance_app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copying folders and application files
# COPY ["./tests", "./src", "./attendace_reports", "./"]
COPY ./tests /attendance_app/tests
COPY ./src /attendance_app/src
COPY ./attendace_reports/ /attendance_app/attendace_reports
COPY ./Readme.md .

CMD [ "python" , "./src/main.py" ]

## TODO: Teams Attendance docker image definition, it must allow to run src.main.py