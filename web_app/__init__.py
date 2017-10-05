import os,requests
from flask import Flask,url_for,render_template,jsonify,request
from flask import make_response




# Define the WSGI application object
app = Flask(__name__)




#gets the email status
def get_json(url,data):
    #url = 'https://mailgnome.herokuapp.com/check_email/'
    email = data['email']
    r = requests.get(url+email.lower());
    print(r)
    data = r.json();
    return data;



@app.route('/')
def index():
    #get complete email list
    return render_template('index.html');

@app.route('/email',methods=['POST'])
def handle_email():
    email = request.form['email']
    url = "http://spiderapi.herokuapp.com/api/email/"
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
    api_url = "https://spiderapi.herokuapp.com/api/email/"
    r = requests.post(api_url,json={"email":email,"key":"C88B933A691E16C56EBC92BCC9A7E"},headers=headers)
    print(r.json())
    return jsonify(r.json()),200