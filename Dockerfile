# Use an official Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /flask-loan-app

# Copy requirements.txt first for better caching
COPY session_7_CD/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files into the working directory
COPY session_7_CD/ .

# Expose the port your app will run on
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]
