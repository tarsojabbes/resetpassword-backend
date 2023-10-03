# ~/.local/bin/uvicorn main:app --reload
import datetime
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(filename='reset.log', level=logging.INFO, format='%(asctime)s - %(message)s')

import secrets

from lcc_ldap import change_pass

load_dotenv()

PASSWORD_LENGTH = int(os.getenv('PASSWORD_LENGTH'))
KEY = os.getenv('KEY')

app = FastAPI()

ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS').split(',')
ALLOWED_METHODS = os.getenv('ALLOWED_METHODS').split(',')
ALLOWED_EMAIL_DOMAINS = os.getenv('ALLOWED_EMAIL_DOMAINS').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=ALLOWED_METHODS,
    allow_headers=["*"],
)

@app.post("/reset_password")
async def create_command(request: Request, response: Response):
    obj = await request.json()
    email, host = obj['email'].split('@')
    print(email, host)
    print(KEY)
    if obj['key'] != KEY or host not in ALLOWED_EMAIL_DOMAINS:
        log_message = f"{email}@{host} couldn't change LDAP password - Unauthorized"
        logging.info(log_message)
        response.status_code = status.HTTP_403_FORBIDDEN
        return str({"status": "forb"})
    if host == 'computacao.ufcg.edu.br':
        email += '.ufcg'
    password = secrets.token_urlsafe(PASSWORD_LENGTH)
    change_pass(email, password)
    return str({"status": "ok", "password": password})
