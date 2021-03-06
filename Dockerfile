FROM python:3.7-buster
RUN apt update -y
RUN apt install ffmpeg -y
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src .
CMD uvicorn run:app --host=0.0.0.0 --port=$PORT
