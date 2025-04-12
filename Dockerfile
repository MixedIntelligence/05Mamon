# File: Dockerfile
# Path: /
# Description: Docker configuration file to containerize the Flask application.

# Use Python as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
