class ineuron:
    def __init__(self):
        self.students1 ="data science"

    def students(self):
        print(self.students1)

i=ineuron()
i.students()
i.students1="data analytics"   # it orerride value of var in runtime , so the output is "data analytics
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 ="data science1"

    def students(self):
        print(self.__students1)
    def student_change(self,new_value):
        self.__students1=new_value

i1=ineuron1()
i1.students()
i1.students1="big data "   # it  cannt orerride value of var in runtime ,becaue it is private var so the output is "data science1"
i1.students()
i1.student_change("shubham")    #but, with the help of class method itself ,we can modify the private variable of same class
i1.students()

# we cannt allow a user to change the value of var directly,so for changing the value of private var we are using a internal class method to change the value of var
#,it is called encapsulation.

#encapsulation: you dont allow user to modify the varible dircectly,so for changing the value of variable we are using a internal class method to change the value of var
#,it is called encapsulation.

#in encapsulation getter and setter method are used
#with the help of setter method we used to modify the variable.  Here in our program in  "def student_change(self,new_value):" is setter method