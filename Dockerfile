FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD [ "uvicorn", "run:app", "--host=0.0.0.0", "--port=${PORT:-8080}" ]
