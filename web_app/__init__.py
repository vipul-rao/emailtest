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
from datetime import datetime
from web_app.permutator import *
# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)

# Define the WSGI application object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
FORMAT = '%Y%m%d%H%M%S'


#gets the email status
def get_json(url,data):
    #url = 'https://mailgnome.herokuapp.com/check_email/'
    email = data['email']
    r = requests.get(url+email.lower());
    print(r)
    data = r.json();
    return data;

#csv parse job pool
def parse_csv_pool(email_list,req_id):
    try:
        #email_list = parse_csv(filename);
        email_list=verify(email_list,req_id);
        print("One job finished!")
    except Exception as e:
        traceback.print_exc()
#    return Response(json.dumps(email_list,  mimetype='application/json'))


#list parse job pool for guessing
def guess_pool(list_email_list,req_id):
    try:
        for email_list in list_email_list:
            parse_csv_pool(email_list,req_id);
        print('guessing file finished!');
    except Exception as e:
        traceback.print_exc();
        
@app.route('/')
def index():
    #get complete email list
    return render_template('index.html');

@app.route('/email',methods=['POST'])
def handle_email():
    email = request.form['email']
    url = "http://spiderapi.herokuapp.com/api/emails/"
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
        req_id = 'file'+datetime.now().strftime(FORMAT)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            try:
                email_list = parse_csv(UPLOAD_FOLDER+filename)
               # print("init.py: email list: ",email_list[0])
                print("init.py: Email list length: ",len(email_list))
                for i in email_list:
                    print(i)
                email_list =[email for email in email_list if email['email'] is not '']
                list_size = len(email_list);
                req_id+='_{0}'.format(list_size);
                print("parsed length:",list_size)
                executor.submit(parse_csv_pool,email_list,req_id)
                return redirect(url_for('results',rid=req_id))
                #return 'One jobs was launched in background with id: {0}'.format(req_id)
            except Exception as e:
                return str(e);
        else:
            return jsonify({'code': 400,'message': 'No interface defined for URL'}),400

@app.route('/results',methods=['GET'])
def results():
    req_id=request.args['rid']
    return render_template('result.html',req_id=req_id);
    

@app.route('/guess',methods=['GET','POST'])
def guess_email():
    if request.method == 'POST':
        req_id = 'file'+datetime.now().strftime(FORMAT)
        fname = request.form['fname']
        lname = request.form['lname']
        dname = request.form['dname']
        e = EmailPermutator()
        email_list = e.get_emails(fname=fname,lname=lname,dname=dname)
        for i,email in enumerate(email_list):
            email_list[i]= {'email':email}
        list_size = len(email_list);
        req_id+='_{0}'.format(list_size);
        print("parsed length:",list_size)
        executor.submit(parse_csv_pool,email_list,req_id)
        #return jsonify({"response":req_id,"url":'/results?rid='+req_id});
        return redirect(url_for('results',rid=req_id))
    return "Hello"
    
    
def recursive_len(item):
    if type(item) == list:
        return sum(recursive_len(subitem) for subitem in item)
    else:
        return 1

@app.route('/guesses',methods=['GET','POST'])
def handle_guessList():
    if request.method == 'GET':
        return "Hello getter"
    elif request.method == 'POST':
        req_id = 'guess'+datetime.now().strftime(FORMAT)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            try:
                guess_list = parse_csv(UPLOAD_FOLDER+filename)
                print("init.py:/guesses: Email list length: ",len(guess_list))
               # print("init.py:/guesses: email list: ",guess_list[0])
                
                # for i in guess_list:
                #     print(i)
                if('firstname' not in guess_list[0].keys()):
                    return 'firstname column not present in csv!';
                elif('lastname' not in guess_list[0].keys()):
                    return 'lastname column not present in csv!';
                elif('domain' not in guess_list[0].keys()):
                    return 'domain column not present in csv!';
                    
                e = EmailPermutator();
               # print("init.py:/guesses: type of list[0]",type(guess_list[0]));
                tmp_list = guess_list;
                for person in tmp_list:
                    person['email'] = e.get_emails(person['firstname'],person['lastname'],person['domain']);
                
                tmp_emails=[];
                for person in tmp_list:
                    each_persons_list = []
                    for email in person['email']:
                        tmp_person = person.copy();
                        tmp_person['email'] = email;
                        each_persons_list.append(tmp_person);
                    tmp_emails.append(each_persons_list);
                
                print("type: tmp_emails[0]",type(tmp_emails[0]));
                
                #tmp_emails2 = [[person.copy()] for person in tmp_list for email in person['email']]
                #print("tmp_emails2",len(tmp_emails2));
                # print("#################");
                # print("init.py: tmp_list: ");
                # print(tmp_emails);
                # print("##################");
              
              #  email_list = [{'firstname':client['firstname'],'lastname':client['lastname'],'domain':client['domain'],'emails':e.get_emails(client['firstname'],client['lastname'],client['domain'])} for client in guess_list];
              #  emails = [[{'email':i,'firstname':client['firstname'],'lastname':client['lastname'],'domain':client['domain']} for i in client['emails']] for client in email_list]
                list_size = recursive_len(tmp_emails);
                req_id+='_{0}'.format(list_size);
                executor.submit(guess_pool,tmp_emails,req_id)
                # return redirect(url_for('results',rid=req_id))
                #return 'One jobs was launched in background with id: {0}'.format(req_id)
                #return str(emails);
                return redirect(url_for('results',rid=req_id))
            except Exception as e:
                print(e);
                return 'Guesses:Something went wrong while parsing, Error: '+str(e);
        else:
            return jsonify({'code': 400,'message': 'No interface defined for URL'}),400
