FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src/app /app/app
COPY src/data /app/data
COPY src/models /app/models

EXPOSE 5000

CMD ["python", "app/main.py"]
