class car:


    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def milage(self):
        print("milage of this car ")

class tata(car):        #eveery thing will inherit from car
    pass

c=car("sold","v6","radial")
print(c)

t= tata("solid1","v5","radial1")
print(t)
print(t.milage())


