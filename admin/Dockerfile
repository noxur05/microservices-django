FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

CMD ["sh", "/app/entrypoint.sh"]
