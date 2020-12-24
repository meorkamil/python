from model import Menu
from model import Customer
from controller import Controller

class View(Menu):

    customer_list = {}

    def showGreet(self):
        greet = ("\n---- Welcome To Mutiara Restaurant ----")
        return greet
    
    def enterCustomerDetails(self):

        print("Please enter your details")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        telNo = input("Enter Telphone No: ")

        customerEntry = Customer(name, address, telNo)
        self.customer_list = customerEntry.customerDic()

    def showMenu(self, menu_dic=Menu.menu_dic):
        print("\n-- This is our menus --")
        for key, value in menu_dic.items():
            print(f"{key}: {value}")

        decision = input("\nYou want to procced ? y/n: ")
        print("------------------------------")

        if decision == "n":
            print("Exit, Thank You")
        else:
            print("Please wait")
            return Controller().calTotal(menu_dic)

    def showCustomer(self):
        print(self.customer_list)

    def showTotal(self, totalPrice):
        print(f"----------------------")
        print(f"Total Price: RM{totalPrice}")
        print(f"--------------------------\n")
        
        decision = input("Proceed to payment? y/n ")

        if decision == "y":
            print("Please wait\n")
            print("----- Payment process ------")
            amount = input("Enter Amount: ")
            return Controller().calPayment(totalPrice, amount)        
        else: 
            print("Exit, Thank You")
    
    def showReceipt(self, balance, totalPrice, amount):
        print("\n------------ Receipt --------------")
        print(f"Total Price: RM{totalPrice}")
        print(f"Paymnet Amount: RM{amount}")
        print(f"Balance: RM{balance}")
        print("-----------------------------------")
        print("Thank You!")
