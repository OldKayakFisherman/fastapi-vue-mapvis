FROM python:3.13.2-slim-bookworm

RUN mkdir app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "main.py", "--port", "5000"]