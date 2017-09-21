from flask import Flask,url_for,render_template

# Define the WSGI application object
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');
	
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

