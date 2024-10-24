
FROM python:3.9.16-slim

RUN apt-get update && apt-get install -y gcc libpq-dev curl

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
EXPOSE 4201

COPY ./src /src

COPY ./bin/run_services.sh /bin/run_services.sh


ENV PYTHONPATH=/src

WORKDIR /src

# Ensure the run_services.sh script is executable
RUN chmod +x /bin/run_services.sh

CMD ["/bin/run_services.sh"]
