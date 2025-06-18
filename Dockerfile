# Using the official Python image as a base image.
FROM python:3.11-slim

# Sets the working directory.
WORKDIR /app

# Copies files from the current directory to the container's main directory.
COPY . /app

# Upgrades pip and install dependencies.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Changes the workdirectory to the application directory.
WORKDIR /app/scieng_website

# Collects the static files.
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Exposes the port to 80 for the Django app.
EXPOSE 80

# Command to run the Django development server on port 80.
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]