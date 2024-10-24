
FROM python:3.9.16-slim

# Install any system dependencies if needed (e.g., for Uvicorn)
RUN apt-get update && apt-get install -y gcc libpq-dev

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the ports for Prefect and FastAPI
EXPOSE 8001
EXPOSE 4201

COPY ./src/web_service /web_service
COPY ./bin/run_services.sh /bin/run_services.sh

WORKDIR /web_service

# Ensure the script is executable
RUN chmod +x /bin/run_services.sh

CMD ["/bin/run_services.sh"]