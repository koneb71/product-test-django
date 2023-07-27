# Use the official Python image as the base image
FROM python:3.9.17-bullseye

# Set environment variables for Python buffering and prevent writing .pyc files
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    gettext \
    postgresql \
    libpq-dev \
    python3-dev

# Install project dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /code/

# Expose the port that the Django development server will use
EXPOSE 8000

# Command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
