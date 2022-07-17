class Person1:
    _name="shubh"
    __surname="chaudhary"
    yob=1009

obj = Person1()
print(obj)

class Employee1(Person1):
    pass

obj1=Employee1()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._Person1__surname)


