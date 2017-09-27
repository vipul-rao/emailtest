import os,requests
from flask import Flask,url_for,render_template,jsonify,request
from flask import make_response
import flask_restful as restful
from flask_pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
#Define the Mongo url
MONGO_URI = os.environ.get('MONGODB_URI')
#MONGO_URI = "mongodb://admin:admin123@ds149134.mlab.com:49134/heroku_2g2nnp30"

if not MONGO_URI:
    MONGO_URI = "mongodb://localhost:27017/api";
print("MONGO_URL: "+MONGO_URI)


# Define the WSGI application object
app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URI

#Initialize mongoDB connection
mongo = PyMongo(app)

#JSON-response builder function
def output_json(obj, code, headers = None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp



#gets the email status
def get_json(url,data):
    #url = 'https://mailgnome.herokuapp.com/check_email/'
    email = data['email']
    r = requests.get(url+email.lower());
    print(r)
    data = r.json();
    return data;        


DEFAULT_REPRESENTATIONS = {'application/json': output_json}

api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS


import web_app.resources


@app.route('/')
def index():
    #get complete email list
    return render_template('index.html');

@app.route('/api/')
def docs():
    #get complete email list
    return render_template('rest-docs.html');

@app.route('/email',methods=['POST'])
def handle_email():
    email = request.form['email']
    url = "http://localhost:8080/api/email/"
    print("requesting: ",url)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url,json={"email":email,"key":"C88B933A691E16C56EBC92BCC9A7E"},headers=headers)
    print(r.json())
    if r.status_code == 200:
        return jsonify(r.json()),200
    else:
        return jsonify({"response":" Something when wrong ","status_code": 400});
    
    
@app.route('/emails',methods=['POST'])
def handle_emailList():
    email = request.form['email']
    headers = {'Content-type': 'application/json'}
    print('here')
    api_url = "https://localhost:8080/api/email/"
    r = requests.post(api_url,json={"email":email,"key":"C88B933A691E16C56EBC92BCC9A7E"},headers=headers)
    print(r.json())
    return jsonify(r.json()),200




    
    

