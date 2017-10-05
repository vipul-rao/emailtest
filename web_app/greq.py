import json,grequests;
json_list = json.loads(open('olive.json').read());
js_list = []
url = "https://spiderapi.herokuapp.com/api/email/"
headers = {'Content-type': 'application/json'}
for i,json_obj in enumerate(json_list):
    js_list.append(json_obj['email'])
rs = (grequests.post(url , json = {"email": mail,"key": "C88B933A691E16C56EBC92BCC9A7E"} , headers = headers) for mail in js_list)
print(rs)
gr = grequests.map(rs)
for r in gr:
    print(r.content)