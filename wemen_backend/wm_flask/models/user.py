from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, EmailField
from flask_login import UserMixin


class User(UserMixin, Document):
    firstname = StringField(max_length=20, unique=True, required=True)
    lastname = StringField(max_length=20, unique=True, required=True)
    email = EmailField(max_length=120, unique=True, required=True)
    password_hash = StringField(max_length=100, required=True)
    marital_status = StringField(max_length=50, required=True)
    country = StringField(max_length=50, required=True)
    created_at = DateTimeField(default=datetime.utcnow())



