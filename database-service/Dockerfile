FROM python:3
ENV PYTHONUNBUFFERED=1
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONUNBUFFERED=1
WORKDIR /db
COPY ./requirements.txt /db/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /db/requirements.txt
COPY . /db
EXPOSE 8000