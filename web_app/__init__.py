import os,requests,json,sys,traceback
from flask import Flask,url_for,render_template,jsonify,request,Response,redirect
from werkzeug import secure_filename
from werkzeug.routing import RequestRedirect
from flask import make_response
from concurrent.futures import ThreadPoolExecutor
from web_app.files_utils import allowed_file,UPLOAD_FOLDER
from web_app.csv2json import parse_csv
from web_app.greq import verify;
from collections import OrderedDict

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

# Define the WSGI application object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
url = "https://spiderapi.herokuapp.com/api/email/"
r=requests.get(url)
print("First request response:",r);
print("JSON: ",r.json())
def print_res(res, **kwargs):
    print(res)
    print(kwargs)

#gets the email status
def get_json(url,data):
    #url = 'https://mailgnome.herokuapp.com/check_email/'
    email = data['email']
    r = requests.get(url+email.lower());
    print(r)
    data = r.json();
    return data;

#csv parse job pool
def parse_csv_pool(filename):
    try:
        email_list = parse_csv(filename);
        email_list=verify(email_list);
        print("One job finished!")
    except Exception as e:
        traceback.print_exc()
#    return Response(json.dumps(email_list,  mimetype='application/json'))
   
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
    
    
@app.route('/emails',methods=['GET','POST'])
def handle_emailList():
    if request.method == 'GET':
        return "Hello getter"
    elif request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            try:
                executor.submit(parse_csv_pool,UPLOAD_FOLDER+filename)
                #email_list = parse_csv(UPLOAD_FOLDER+filename)
                return 'One jobs was launched in background!'
            except Exception as e:
                return str(e);
        else:
            return jsonify({'code': 400,'message': 'No interface defined for URL'}),400
            
