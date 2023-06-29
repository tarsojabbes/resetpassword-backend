# ~/.local/bin/uvicorn main:app --reload
import os

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request, Response, status
import datetime
import logging

logging.basicConfig(filename='reset.log', level=logging.INFO, format='%(asctime)s - %(message)s')

import secrets

from lcc_ldap import change_pass

password_length = 13

KEY = os.getenv('KEY')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/reset_password")
async def create_command(request: Request, response: Response):
    obj = await request.json()
    email, host = obj['email'].split('@')
    print(email, host)
    print(KEY)
    if obj['key'] != KEY or host not in ['ccc.ufcg.edu.br', 'computacao.ufcg.edu.br']:
        log_message = f"{email}@{host} couldn't change LDAP password - Unauthorized"
        logging.info(log_message)
        response.status_code = status.HTTP_403_FORBIDDEN
        return str({"status": "forb"})
    if host == 'computacao.ufcg.edu.br':
        email += '.ufcg'
    password = secrets.token_urlsafe(password_length)
    change_pass(email, password)
    return str({"status": "ok", "password": password})