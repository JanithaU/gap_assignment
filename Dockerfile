FROM python:3.10

WORKDIR /django

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

# Environment
RUN apt-get update
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copy our codebase into the container
COPY . .
