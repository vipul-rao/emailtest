import chardet,json,shlex
import csv
from collections import OrderedDict

def predict(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)
    



class csvReader:
   
    def __init__(self,f):
        self.f = f;
        self.header = None;
        self.pos = None
        
    def __iter__(self):
        with open(self.f,'rb') as file:
            for i,line in enumerate(file):
                try:
                    line = line.decode('utf-8')
                except Exception as e:
                    print('Exception in line {0} , Exception type: {1}'.format(i,type(e).__name__))
                    encoding_dict = chardet.detect(line)
                    print('Detected encoding: ',encoding_dict)
                    print ('old string: ',line.strip())
                    line = line.decode(encoding_dict['encoding'])
                    print('new string: ',line)
                    
                if i==0:
                    self.header = line.lower().strip().split(',')
                    for j,head in enumerate(self.header):
                        if 'email' in head:
                            self.pos = j;
                        
                    if self.pos==None:
                        raise Exception("No email found in header, make sure file has an `email` column in header!")
                    self.header.insert(self.pos+1,'status')
                else:
                    
                    reader = csv.reader([line.strip()], skipinitialspace=True)
                    line = next(reader)
                    #line = line.strip().split(',');
                    line.insert(self.pos+1,'')
                    yield OrderedDict(zip(self.header,line))
            else:
                raise StopIteration
        
                    


class csv2dict:
    def __init__(self,f):
        self.f = f;
        self.reader = csvReader(f)
    
    def to_json(self):
        lst = []
        for item in self.reader:
            yield item
        #     lst.append(item)
        # return lst;

#reader = csvReader('test.csv');
c2d = csv2dict('test.csv')
json_generator = c2d.to_json()

jsonlist = [i for i in json_generator];

with open('test.json','w') as f:
    # for item in jsonGenerator:
    #     jsonlist.append(item)
    
    print("Length of list now:",len(jsonlist))
    f.write(json.dumps(jsonlist))
    
print(predict('olive.json',n_lines=500))

# with open('test3.json','w') as f:
#     f.write('[\n')
#     for json_obj in jsonlist:
#         f.write("{")
#         for key,value in json_obj.items():
#             f.write("\"{0}\" : \"{1}\",".format(key,json_obj[key]))
#         f.write("},")
#     f.write(']')

