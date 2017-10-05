import json
from collections import OrderedDict

def read_json(f):
    with open(f,"r",encoding="UTF-8") as file:
        return json.loads(file.read(),object_pairs_hook=OrderedDict);
        
def json2csv(f,f2):
    json_list = read_json(f)
    csv_data = ""
    with open(f2,"w",encoding="UTF-8") as file:
        file.write(",".join([key for key in json_list[0].keys()]))
        for json_data in json_list:
            file.write("\n"+",".join(json_data.values()))

json2csv("test9.json","test10.csv")

def predict(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)
    
print("Prediction: {0}".format(predict("test10.csv",n_lines=501)))
        