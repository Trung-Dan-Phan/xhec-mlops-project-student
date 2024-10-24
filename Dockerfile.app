# Use a lightweight Python image
FROM python:3.9.16-slim

# Install any system dependencies if needed (e.g., for Uvicorn)
RUN apt-get update && apt-get install -y gcc libpq-dev curl

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
EXPOSE 4201

COPY ./src /src

COPY ./bin/run_services.sh /bin/run_services.sh


ENV PYTHONPATH=/src

WORKDIR /src

# Ensure the run_services.sh script is executable
RUN chmod +x /bin/run_services.sh

# Run the services using the script
CMD ["/bin/run_services.sh"]
