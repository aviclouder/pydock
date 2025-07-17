FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN sleep 30s


# If building and running this without using docker-compose, uncomment the below code, before proceeding.

CMD [ "python", "app.py" ]
