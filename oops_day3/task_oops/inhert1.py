class Sitaram:
    def __init__(self,name,father_name,mother_name,dob):
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.dob=dob
    def Show_details(self):
        print("apun ka naam",self.name,"baap ka naam",self.father_name,"maa ka naam",self.mother_name,"janam kundali",self.dob)

class Ramesh:
    def __init__(self,name,father_name,mother_name,dob):    #constructor: used to initilized class members
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.dob=dob
r=Sitaram("sitaram ","banshraj ","lola ","12/12/1222")
r.Show_details()

#****************************************************************************************************************************************

class Sitaram:
    def __init__(self,name,father_name,mother_name,dob):
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.dob=dob
    def Show_details(self):
        print("apun ka naam",self.name,"baap ka naam",self.father_name,"maa ka naam",self.mother_name,"janam kundali",self.dob)

class Ramesh(Sitaram):
    def __init__(self,name,father_name,mother_name,dob):    #constructor: used to initilized class members
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name
        self.dob=dob
s=Sitaram("sitaram ","banshraj ","lola ","12/12/1222")
r=Ramesh("ramesh ","sitaram ","janarma ","12/12/1982")
r.Show_details()
