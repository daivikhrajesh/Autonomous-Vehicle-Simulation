# Base image for Python environment
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port used by your application (if any) # Replace with the actual port if used
EXPOSE 6000  

# Command to run the application
CMD [ "python", "main.py" ]
