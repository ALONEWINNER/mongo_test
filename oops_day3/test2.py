#multiple inhertainece

class bank:
    def transcation(self):
        print("tottal transaltion value")
    def Account_opening(self):
        print("show account open status")
    def deposite(self):
        print("your deposited amont is here")
    def test(self):
        print("test method of bank")


class HDFC_bank():
    def hdfc_to_icici(self):
        print("tansaction happening through hdfc")

    def test(self):
        print("test method of hdfc")


class ineuron_bank:
    def account_status_icici(self):
        print("bank status of icici")

class icici(bank,HDFC_bank,ineuron_bank):                    #multiple inhertance
    pass

i = icici()
i.deposite()
i.Account_opening()
i.hdfc_to_icici()
i.transcation()
i.test()
i.account_status_icici()