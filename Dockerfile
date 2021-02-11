FROM python:3.7-buster
RUN apt update -y
RUN apt install ffmpeg -y
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src .
ENV PORT 8080
ENV BOT_TOKEN 1465677221:AAFyhuAI0ZWi_K7KF21zOeODZUiP3AgP-KU
CMD [ "uvicorn", "run:app", "--host=0.0.0.0", "--port=5000" ]
