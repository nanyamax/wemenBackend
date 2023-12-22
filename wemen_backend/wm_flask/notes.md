models.py contains all the database models for the website
views.py is used to store all the main views(standard route where users can actually go to eg homepage) or the url endpoint for the actual functioning frontend aspect of the website
any routes that needs authentication will be placed in the auth file while other routes like the homepage or the about etc will be placed the the views.py file


from flask import Flask, render_template
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config
db = MongoEngine(app)


@app.route('/')
def home():
    return 'Navigating your world as a woman'


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
