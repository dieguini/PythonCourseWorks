FROM python:alpine3.16
LABEL version="1.2.0"

WORKDIR /attendance_app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copying folders and application files
# COPY ["./tests", "./src", "./attendace_reports", "./"]
COPY ./tests /attendance_app/tests
COPY ./src /attendance_app/src
COPY ./attendace_reports/ /attendance_app/attendace_reports
COPY ./Readme.md .

ENTRYPOINT [ "python" , "./src/main.py" ]
