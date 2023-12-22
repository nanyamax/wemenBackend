import json

from flask import Blueprint, url_for, request, redirect, flash, render_template
import flask
from flask_cors import cross_origin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .models import User
from .utils.password import hashPassword, checkHashedPassword


auth = Blueprint('auth', __name__)
login_manager = LoginManager()
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


@auth.route('/login', methods=['POST'])
@cross_origin()
def login():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'POST':
        jsonData = request.json
        email = jsonData.get("email")
        password = jsonData.get("password")
        print(jsonData.get("email"))
        
        user = User.objects(email=email).first()
        if user:
            if checkHashedPassword(user.password, password):
                dataToReturn = {
                    "email" : user.email,
                    "firstName" : user.firstName,
                    "lastName": user.lastName,
                    "maritalStatus" : user.maritalStatus,
                    "country" : user.country,
                    "created_at" : user.created_at
                }
                login_user(user, remember=True)
                return dataToReturn
            else:
                return {"status" : "Invalid email/password"}
        else:
            return {"status" : "Email does not exist"}
    else:
        return {"Error" :"Invalid request"} 


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    if request.method == 'POST':
        jsonData = request.json
        email = jsonData.get('email')
        firstName = jsonData.get('firstName')
        lastName = jsonData.get('lastName')
        password = jsonData.get('password')
        password2 = jsonData.get('password2')
        user = User.objects(email=email).first()
        if user:
            return {"status" : "Email already in use"}
        elif not email and len(email) < 5:
            return {"status" : "Invalid email address"}
        elif not firstName or len(firstName) < 2:
            return {"status" : "Invalid first name"}
        elif not lastName or len(lastName) < 2:
            return {"status" : "Invalid last name"}
        # elif  not password or not password2 or len(password) < 8:
        #     return {"status" : "Password must be at least 8 characters."}
        elif password != password2:
            print(password, password2)
            return {"status" : "Both password do not match"}
        else:
            print(jsonData)
            hashedPassword = hashPassword(password)
            print(hashedPassword)
            result = User(email=email, firstName=firstName, lastName=lastName, password = hashedPassword).save()
            return {"status" : "Done"}


