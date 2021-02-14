from .response import Response
from .helper import *
from .models import *


class Authentication(Response):
    def user_registration(self, data):
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        dob = data['dob']
        address = data['address']

        if (not username or not password) or (username == "" or password == ""):
            self.set_status_code(400)
            self.set_content("username and password cannot be empty.")

            return self.get_response()

        if User.query.filter_by(username=username).first():
            self.set_status_code(400)
            self.set_content("user already exist.")

            return self.get_response()

        new_user_id = User(username=username, password=password,
                           first_name=first_name, last_name=last_name, dob=dob, address=address)
        db.session.add(new_user_id)
        db.session.commit()

        self.set_status_code(200)
        self.set_content("user has been created.")

        return self.get_response()

    def user_login(self, data):
        username = data['username']
        password = data['password']

        user_id = User.query.filter_by(username=username).first()

        if user_id:
            try:
                if user_id.verify_password(password):
                    
                    if user_id.is_logged_in:
                        self.set_status_code(400)
                        self.set_content("user have been logged in another device.")
                        
                        return self.get_response()
                    
                    user_id.is_logged_in = True
                    db.session.commit()
                    
                    token_data = {
                        'id': user_id.id,
                        'username': user_id.username,
                        'first_name': user_id.first_name,
                        'last_name': user_id.last_name
                    }

                    token = encode_token(token_data)

                    self.set_status_code(200)
                    self.set_content({'user_id': user_id.id, 'username': user_id.username, 'token': token.decode('utf-8')})

                return self.get_response()

            except Exception as e:
                self.set_status_code(400)
                self.set_content("invalid credentials.")

                return self.get_response()
        else:
            self.set_status_code(404)
            self.set_content("user not found.")

            return self.get_response()
    
    def user_logout(self, payload):
        payload = decode_token(payload)
        
        if payload:
            user_id = User.query.filter_by(username=payload['username']).first()
            
            if user_id:
                user_id.is_logged_in = False
                db.session.commit()
            
            self.set_status_code(200)
            self.set_content("logged out.")
            
            return self.get_response()
        else:
            self.set_status_code(400)
            self.set_content("invalid credentials.")
            
            return self.get_response()
