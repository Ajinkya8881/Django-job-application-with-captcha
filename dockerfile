# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set the CMD to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
