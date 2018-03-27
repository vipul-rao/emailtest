class EmailPermutator():
    special_chars = ['.']
    

    def __init__(self,fname='',lname='',dname=''):
        self.fname = fname
        self.lname = lname
        self.dname = dname
    
    def get_fname(self):
        return self.fname
    
    def set_fname(self,fname):
        self.fname = fname
    
    
    def get_lname(self):
        return self.lname
    
    def set_lname(self,lname):
        self.lname = lname
        
    
    def get_dname(self):
        return self.dname
    
    def set_dname(self,dname):
        self.dname = dname
    
    def get_emails(self,fname,lname,dname):
        self.fname = fname;
        self.lname = lname;
        self.dname = dname;
        
        email_list = []
        email_list.append(self.fname+'@'+self.dname)
        email_list.append(self.fname[:1]+self.lname+'@'+self.dname)
        email_list.append(self.fname+self.lname+'@'+self.dname)
        email_list.append(self.fname+self.lname[:1]+'@'+self.dname)	
        email_list.append(self.fname[:1]+self.lname[:1]+'@'+self.dname)	
	email_list.append(self.lname+'@'+self.dname)
        email_list.append(self.fname[:1]+'.'+self.lname+'@'+self.dname)
        
        for char in self.special_chars:
            email_list.append(self.fname+char+self.lname+'@'+self.dname)
            email_list.append(self.fname[:1]+char+self.lname+'@'+self.dname)
        
        return email_list

