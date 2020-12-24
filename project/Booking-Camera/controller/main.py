from model.user import User

class MainController:

    def getUserDetails( self, name, age, address, notel):
        user = User(name, age, address, notel)
        return user.showPerson()

