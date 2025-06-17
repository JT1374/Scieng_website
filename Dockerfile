# Using the official Python image as a base image.
FROM python:3.10-slim

# Sets the working directory in the container.
WORKDIR /app

# Copies files from the current directory to the container's main directory.
COPY . /app

# Upgrade pip and install dependencies.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Changes the workdirectory to the
WORKDIR /app/scieng_website

# Collects the static files.
RUN python manage.py collectstatic --noinput

# Exposes the port to 80 for the Django app.
EXPOSE 80

# Command to run the Django development server on port 80.
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]