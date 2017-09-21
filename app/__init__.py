from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

@app.route('/')
def index():
	return "HELLO WORLD!"

