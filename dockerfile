# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy both requirements.txt and the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set environment variable
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "app.py"]
