FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache build-base openldap-dev python3-dev && \
  pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "/usr/local/bin/uvicorn" ]

CMD [ "main:app", "--port", "5000", "--host", "0.0.0.0" ]
