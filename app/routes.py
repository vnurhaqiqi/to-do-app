from app import app
from flask import request

from .services import *
from .helper import *

auth = Authentication()


@app.route(BASE_URL + 'registration', methods=['POST'])
def registration():
    body = request.get_json()

    if request.method == 'POST':
        service = auth.user_registration(body)

    return service

@app.route(BASE_URL + 'login', methods=['POST'])
def login():
    body = request.get_json()
    
    if request.method == 'POST':
        service = auth.user_login(body)
    
    return service

@app.route(BASE_URL + 'logout', methods=['POST'])
def logout():
    token = request.headers['token']
    
    if request.method == 'POST':
        service = auth.user_logout(token)
        
    return service