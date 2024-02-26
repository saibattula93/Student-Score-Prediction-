# Use the official Python base image with a specific version
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt

# Expose the port your application listens on (use port 5000)
EXPOSE 5000

# Command to run your application (replace 'app.py' with your actual script name)
CMD ["python", "app.py"]