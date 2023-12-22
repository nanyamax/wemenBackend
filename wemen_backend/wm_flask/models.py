from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, EmailField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, Document):
    firstName = StringField(max_length=20, required=True)
    lastName = StringField(max_length=20, required=True)
    email = EmailField(max_length=120, unique=True, required=True)
    password = StringField(required=True)
    maritalStatus = StringField(max_length=50)
    country = StringField(max_length=50)
    created_at = DateTimeField(default=datetime.utcnow())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


