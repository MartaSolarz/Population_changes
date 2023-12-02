FROM python:3.9.5-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["voila", "main.ipynb", "--no-browser", "--port=8080", "--Voila.base_url=/", "--Voila.ip=0.0.0.0"]

