# data abstraction: if we are not giving access to user(object) to access a data inside a class directly,
# it will first go to class then that variable/method
#hide most of thing from rest of world, show only abstract part only

class ineuron:
    __student="data science"   #private var

    def students(self):
        print("print the class of ",ineuron.__student,"student")

i=ineuron()  # it can access all clss meembers and variable of ineuron
i.students()
#i.__student   # caant access the data from class i.e. data abstractio(data hiding)
# to access __student , we ahev to go first class then data
print(i._ineuron__student)


