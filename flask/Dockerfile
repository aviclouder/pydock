FROM python:alpine3.21

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# This will help to start all the services of MySql to start prior to launch the flask application.
# If using docker compose, comment this 
# RUN sleep 30s

# If building and running this without using docker-compose, uncomment the below code, before proceeding.

CMD [ "python", "app.py" ]
