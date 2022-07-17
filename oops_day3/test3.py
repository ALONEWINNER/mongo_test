# method overriding
## this is called method overriding: in inhertainece when we try to redefine/override a method which is already exist in parent class,
# so during calling modest(child class's method) override previous (base) one.

# sati pratha is override by new concept of alive after husband_dead

class ineuron:
    def student(self):
        print("all students details")

    def acchivers(self):
        print("list of accivers")

    def hall_of_frame(self):
        print("hall of frame")

class ineuron_vision(ineuron):

    def student(self):
        print("these  are filtered studnet list")

iv=ineuron_vision()
iv.student()        # it will give  call the lastest method(child)  o/p:"these  are filtered studnet list"
# this is called method overriding: in inhertainece when we try to redefine/override a method which is already exist in parent class, so during calling modest one override previous (base) one.