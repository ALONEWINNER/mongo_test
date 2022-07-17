#multilevel inhertainece

class bank:
    def transcation(self):
        print("tottal transaltion value")
    def Account_opening(self):
        print("show account open status")
    def deposite(self):
        print("your deposited amont is here")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("tansaction happening through hdfc")

class icici(HDFC_bank):
    pass

d = icici()
d.transcation()
d.hdfc_to_icici()
d.deposite()
d.Account_opening()

