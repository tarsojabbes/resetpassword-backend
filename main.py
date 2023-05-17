# ~/.local/bin/uvicorn main:app --reload
import os

from dotenv import load_dotenv

from fastapi import FastAPI, Request, Response, status

import secrets

from lcc_ldap import change_pass

password_length = 13

KEY = os.getenv('KEY')

app = FastAPI()

@app.post("/reset_password")
async def create_command(request: Request, response: Response):
    obj = await request.json()
    email, host = obj['email'].split('@')
    print(email, host)
    if host not in ['ccc.ufcg.edu.br', 'computacao.ufcg.edu.br']:
        response.status_code = status.HTTP_403_FORBIDDEN
        return str({"status": "forb"})
    if host == 'computacao.ufcg.edu.br':
        email += '.ufcg'
    password = secrets.token_urlsafe(password_length)
    change_pass(email, password)
    return str({"status": "ok", "password": password})