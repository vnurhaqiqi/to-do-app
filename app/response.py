from .helper import *
from flask import jsonify


class Response():
    status_code = 200
    content = None
    paging = {}
    message = ""
    
    def set_status_code(self, code):
        self.status_code = code
        self.message = STATUS_CODE[code]
        
    def set_not_found(self):
        self.status_code = 404
        self.message = STATUS_CODE[404]
        
    def set_content(self, content):
        self.content = content
        
    def get_response(self):
        response = {
            'status': self.status_code,
            'message': self.message,
            'content': self.content,
        }
        
        return jsonify(response)
