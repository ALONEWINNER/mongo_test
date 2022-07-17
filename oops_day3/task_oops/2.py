# class-1
class Animal1:
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender

    def show(self):
        print("animal name is=", self.name, "breed=",self.breed, "gender=",self.gender)

class Human:
    pass

a = Animal1("cow","kaira","male")
print(a)
a.show()