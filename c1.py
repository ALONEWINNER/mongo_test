#class is just a classification
# constructor is just a funtion which is used to provide data to clAASS
#__init__ it is a inbuilt method to pass data to class member.
class Person1:
    pass


class Person:
    def __init__(self,name,surname,emailid,Year_of_birth):           #class ke andr function ka furst parameter pointer hota h

        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.Year_of_birth=Year_of_birth

anuj_var= Person("anuj","chaude","llol@gmail.com",1999)  #object= class variable

gsrgi_var= Person("anuja","chahude","lol@gmail.com",1990)

sudh_var= Person("anika","chaunjde","lloli@gmail.com",1989)
print(anuj_var.emailid)
print(anuj_var.name)
print(anuj_var.Year_of_birth)
print(anuj_var)
