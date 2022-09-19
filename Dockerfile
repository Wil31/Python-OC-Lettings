# syntax=docker/dockerfile:1

# Pull official base image
FROM python:3.10

# Set the WORKDIR
WORKDIR /code
ENV PORT=8000

COPY requirements.txt /code/

# Upgrade pip and install requirements 
RUN pip install --upgrade pip \ 
    && pip install -r requirements.txt
EXPOSE 8000

# Copy project 
COPY . /code/

# Collect static files
RUN python manage.py collectstatic

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]