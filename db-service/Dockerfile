FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Run updates
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# Update pip
RUN python -m pip install --upgrade pip

# Install required libraries
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# Copy source code into working diretory
COPY . /app/