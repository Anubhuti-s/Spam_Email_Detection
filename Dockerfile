# Deploy Machine Learning Models Using Docker And Github Action In Heroku Cloud
FROM python:3.9-slim

EXPOSE 8080

WORKDIR /app 
COPY . /app

# install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"] 