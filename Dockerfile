# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt, seperated to cache layer
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run my_script.py when the container launches
CMD ["python", "test.py"]

