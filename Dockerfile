FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the working directory
COPY main.py .

# Set the environment variable to run the application
ENV FLASK_APP=main.py

# Expose the port on which the Flask application will run
EXPOSE 8080

# Start the Flask application when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

