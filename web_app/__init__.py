import os,requests
from flask import Flask,url_for,render_template,jsonify,request
from flask import make_response
#Define the Mongo url


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

@app.route('/emails',methods=['POST'])
def handle_emails():
    email = request.form['email']
    headers = {'Content-type': 'application/json'}
    print('here')
    api_url = "https://spiderapi.herokuapp.com/api/email/"
    r = requests.post(api_url,json={"email":email,"key":"C88B933A691E16C56EBC92BCC9A7E"},headers=headers)
    print(r.json())
    return str(r.json())
	
#  if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8080,debug=True)

