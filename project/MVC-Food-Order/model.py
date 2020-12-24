class Customer:
    

    def __init__(self, name, address, telNo):
        self.name = name
        self.address = address
        self.telNo = telNo
    
    def setName(self):
        self.name = name 

    def getName(self):
        return self.name

    def setAddress(self):
        self.address = address
    
    def getAddress(self):
        return self.address 

    def setTelNo(self):
        self.telNo = telNo

    def getTelNo(self):
        return  self.address     

    def customerDic(self):
     
        customer_dic = {
            "name": self.name,
            "address": self.address,
            "telNo": self.telNo
        }
        return customer_dic


class Menu:

    menu_dic = {
            "Menu": "Nasi Ayam",
            "Price": 10
        }

    def menuList(self):
        return self.menu_dic