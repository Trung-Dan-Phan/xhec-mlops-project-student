#!/bin/bash

echo "PYTHONPATH is $PYTHONPATH"

prefect server start --host 0.0.0.0 --port 4201 &

echo "Waiting for Prefect Server to start..."
until curl -s http://localhost:4201/api/health; do
  sleep 1
done
echo "Prefect Server is up and running."

uvicorn web_service.main:app --host 0.0.0.0 --port 8001
