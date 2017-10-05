import json,requests
from collections import OrderedDict;
json_list = json.loads(open('olive.json',"r").read(),object_pairs_hook=OrderedDict)

for i,json_obj in enumerate(json_list):
    email = json_obj['email']
    url = "http://spiderapi.herokuapp.com/api/email/"
    print(i,") requesting: ",url)
    headers = {'Content-type': 'application/json'}
    r = requests.post(url,json={"email":email,"key":"C88B933A691E16C56EBC92BCC9A7E"},headers=headers)
    print(r.json())
    if r.status_code == 200:
        json_list[i]['status'] = r.json()['message']
    else:
        json_list[i]['status'] = "Mission failed"

with open('olive2.json','w') as f:
    f.write(json.dumps(json_list))
    