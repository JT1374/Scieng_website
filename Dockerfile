# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory to the Django project directory
WORKDIR /app/scieng_website

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 80
EXPOSE 80

# Command to run the Django development server on port 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]