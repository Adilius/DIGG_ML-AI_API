FROM python:3.9-slim

# Run updates
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# Set working directory
WORKDIR /app

# Update pip
RUN python -m pip install --upgrade pip

# Install required libraries
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy source code into working directory
COPY . /app/