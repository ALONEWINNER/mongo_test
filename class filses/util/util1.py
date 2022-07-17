class Person3:
    def __init__(self,name,surname,yob):
        self._name1=name
        self.__surname1=surname
        self.yob=yob

sudh=Person3("shubham","chau",1990)
print(sudh._Person3__surname1)
print(sudh._name1)