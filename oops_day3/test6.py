class ineuron:
    def students(self):
        print("print studnet details")

class class_type:
    def students(self):
        print("print the class type of studetns")

def ineuron_external(a):
    a.students()

#ploymerphism in method(class and objects)
i=ineuron()
j=class_type()
ineuron_external(i)  #object of ineurnon
ineuron_external(j)  #object of class_type


def test(a,b):
    return a+b
#polymerphism in variables

print(test(3,4))  # add two no
print(test("shubham","chaudhary"))  #concatination

#polymorphism: one prson multiple behaviour according to change in curcimstances
#it will be in variable,methods
