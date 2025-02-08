# Use an official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements files and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the microservice code to the container
COPY . .

# Expose the port on which the service will run
EXPOSE 5005

# Set the environment variable for production
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "app.py"]