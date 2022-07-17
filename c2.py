class person:

    def age(self, cur,dob_year):
        return cur-dob_year
    def email_id_input(self,email_id):
        print("email id ",email_id)
    def ask_name(self,name):
        name=print(input("enter your name mamu"))
        return name
    def ask_dob(self):
        dob=input("tell dob mamu")
        return dob
s=person()
p=person()
q=person()
r=person()

s.age(100,34)
s.ask_dob()
s.ask_name("hira")
s.email_id_input("dhjshfjhj")