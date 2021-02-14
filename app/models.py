from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///to_do_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String())
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32))
    dob = db.Column(db.Date())
    address = db.Column(db.Text())
    is_logged_in = db.Column(db.Boolean(), default=False)
    todo_list = db.relationship('Todo', backref='user_todo', lazy='dynamic')

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
        
        return self.password_hash

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, first_name, last_name, dob, address):
        self.username = username
        self.password = self.hash_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = address

    def __repr__(self):
        return f"User {self.username}"


class Todo(db.Model):
    __tablename__ = 'to_do_list'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text())
    date = db.Column(db.Date())
    is_active = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    
    def __init__(self, title, description, date, is_active):
        self.title = title
        self.description = description
        self.date = date
        self.is_active = is_active
        
    def __repr__(self):
        return f"To Do {self.title}"