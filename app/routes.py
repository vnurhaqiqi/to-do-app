from app import app
from flask import request

from .services import *
from .helper import *

auth = Authentication()
todo = TodoList()


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


@app.route(BASE_URL + 'to-do-list', methods=['GET'])
def to_do_list():
    token = request.headers['token']

    if request.method == 'GET':
        service = todo.get_to_do_list(payload=token)

    return service


@app.route(BASE_URL + 'create-to-do', methods=['POST'])
def create_to_do():
    token = request.headers['token']
    body = request.get_json()

    if request.method == 'POST':
        service = todo.create_to_do_data(data=body, payload=token)

    return service


@app.route(BASE_URL + 'update-to-do', methods=['POST', 'PUT'])
def update_to_do():
    token = request.headers['token']
    body = request.get_json()
    params = request.args

    if request.method in ['POST', 'PUT']:
        service = todo.update_to_do_data(
            data=body, params=params, payload=token)

    return service


@app.route(BASE_URL + 'delete-to-do', methods=['DELETE'])
def delete_to_do():
    token = request.headers['token']
    params = request.args

    if request.method == 'DELETE':
        service = todo.delete_to_do_data(params=params, payload=token)

    return service
