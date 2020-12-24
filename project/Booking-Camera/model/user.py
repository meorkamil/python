from model.person import Person

class User(Person):

    def __init__(self, name, age, address, notel):
        
        super().__init__(name, age, address, notel)
    