from flask_login import LoginManager
from wm_flask import create_app 
from mongoengine import *




cloudUri = 'mongodb+srv://ifunanyasunday7:58tnZeQYOUBG7nQt@wemen-dev.esx5cjc.mongodb.net/?retryWrites=true&w=majority'

connect(host=cloudUri)
app = create_app() 
app.config['SECRET_KEY'] = 'secretkey'


if __name__ == '__main__':
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    app.run(debug=True)
