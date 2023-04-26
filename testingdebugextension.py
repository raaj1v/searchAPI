from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.debug = True
toolbar = DebugToolbarExtension(app)

app.config['SECRET_KEY'] = 'secretKeyforDebugging'

toolbar = DebugToolbarExtension(app)

