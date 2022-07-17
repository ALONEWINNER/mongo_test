class ineuron:
    __subject_name="data science"   #private var
    __class_name="Science IT"


    def student_class(self):
        print("print the class of ",ineuron.__class_name,"student")
    def sub_name(self):
        print("subject name is ",ineuron.__subject_name)

i=ineuron()  # it can access all clss meembers and variable of ineuron
i.student_class()
#i.__student   # caant access the data from class i.e. data abstractio(data hiding)
# to access __student , we ahev to go first class then data
print(i._ineuron__subject_name)


#2.
class Blackmoney:
    __total_no_of_account=23000
    __Bankname ="swiss"

    def __Accountname(self,name,dob,acc):
        self.name=name
        self.dob=dob
        self.accountno=acc
        print(self.name,dob,acc)

    def cal(self, amt, rate, year):
        bonus = ((self.amt) * (self.rate) * (self.year)) / 100
        return bonus

    def AccNo(self,amt,rate,year):
        self.amt=amt
        self.rate=rate
        self.year=year
        d= self.cal(self.amt, self.rate, self.year)
        print("bank name is ",Blackmoney.__Bankname,"amount =",self.amt," rate=",self.rate," year=",self.year,"interst=",d)


b=Blackmoney()
b._Blackmoney__Accountname("shubham","02/02/1998",3143000100175339)  #we cannt see details of shubham directly
b.AccNo(4000,5,5)

#ab3

class Ineuron:
    no_of_students=1110
    __no_of_WFH_staff=50
    __no_of_office_staff=60

    def __init__(self, class_type ,strength):
        self.class_type=class_type
        self.strength=strength
        d=self.class_type+self.strength


    def Print_details(self):
        print("total strength of class is ",self.no_of_students)
        print("total strength of WFH staff is ", self.__no_of_WFH_staff)




I=Ineuron('kid',' 70')

I.Print_details()
print("total strength of office staff is ",I._Ineuron__no_of_office_staff)










