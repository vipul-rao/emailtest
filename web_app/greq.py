import json,grequests,requests,time,traceback;
from collections import OrderedDict
url = "http://spiderapi.herokuapp.com/api/email/"
headers = {'Content-type': 'application/json',"Connection": "close"}
MAX_CONNECTIONS = 50


def print_res(res, **kwargs):
    print(res)
    print(kwargs)

def verify(json_list,req_id):
    print("greq.py: url:",url)
    req_id = req_id+'/'
    #response = requests.delete(url+req_id)
    #print("Delete:",response.json())
    #order = ",".join([key for key in json_list[0].keys()])
    #print("greq.py: Order: ",order)
    for i in json_list:
        i['key'] = "C88B933A691E16C56EBC92BCC9A7E";
       # i['order'] = order
    email_list = json_list
    
   
    
    gr=[]
    
    for x in range(0,len(email_list)+1, MAX_CONNECTIONS):
        rs = (grequests.post(url+req_id, stream=False,headers=headers,json=i,hooks=dict(response=print_res)) for i in email_list[x:x+MAX_CONNECTIONS] if i['email'] is not '')
        time.sleep(7) #You can change this to whatever you see works better. 
        gr.extend(grequests.map(rs)) #The key here is to extend, not append, not insert. 
        print("Waiting") #Optional, so you see something is done. 
    
    # print("Length: ", len(email_list))
    # rs = (grequests.post(url ,json = i , headers = headers,hooks=dict(response=print_res)) for i in email_list)
    # #print(rs)
    # gr = grequests.map(rs)
    res =[]
    for r in gr:
        try:
            res.append(r.json(object_pairs_hook=OrderedDict))
        except Exception as e:
            traceback.print_exc()
            
    return res;

# req = (requests.post(url , json = {"email": mail,"key": "C88B933A691E16C56EBC92BCC9A7E"} , headers = headers) for mail in js_list)
# for r in req:
#     print(r);
    
