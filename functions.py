from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route('/register')
def registration_form():
    """Show form for user signup"""



if __name__ == '__main__':
    app.run(debug=True)