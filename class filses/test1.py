#import test2           # we can access eveery thing of test2 here now
import test2

from test2 import Person1
print(test2)

obj3=test2.Person1()  # create obj of test2 file's Person1 class
print(obj3.yob)

#import util.util1 or
from util.util1 import Person3

obj4=Person3("tina","patel",199998)
print(obj4)
print(obj4.yob)



class Person:
    _name="shubh"
    __surname="chaudhary"
    yob=1009

    def _age(self,cur_year):
        return cur_year - self.yob

    def __age1(self,cur_year):
        return cur_year - self.yob




obj = Person()
print(obj._age(2019))
print(obj._Person__age1(2018))
print(obj)

class Employee(Person):
    _name="sonam"                   # this new will be refected now as o/p  not value of pareent class
    __surname = "sahni"
    yob=2000


obj1=Employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._Employee__surname)
print(obj1._age(89))
print(obj1._Person__age1(199))

