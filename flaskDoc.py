from flask import Flask

from flask import request 
from flask import url_for
from markupsafe import escape 

app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method=='POST':
#         return "userr_logged_in"
#     else:
#         return "show_llogin_form"


@app.route('/')
def Default():
    return 'Default Page'


@app.route('/greet')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return "Index Page"

@app.route('/user/<username>')

def index2(username):
    print("username", username)
    return f"INDEX_  {escape(username)}"

