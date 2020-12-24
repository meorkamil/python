from model.cameraman import Cameraman
from controller.main import MainController

class MainView:

    def showGreet(self):
        print("Hello!, Welcome to Phographer!")

    def showCameraman(self):
        cameraman = Cameraman().showCameraman()
        for key, value in cameraman.items():
            print(f"{key}: {value}")
    
    def inputUserDetails(self):
        name = input("Enter Your Name: ")
        address = input("Enter Address: ")
        notel = input("Enter Your NoTel: ")
        age = input("Enter Your age: ")
        
        return MainController().getUserDetails(name, age, address, notel)