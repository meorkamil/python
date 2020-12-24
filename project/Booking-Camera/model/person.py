class Person:

    def __init__(self, name, age, address, notel):
        self.name = name
        self.age = age
        self.address = address
        self.notel = notel

    def showPerson(self):

        person_list = {
            "Name": self.name,
            "Age": self.age,
            "Address": self.address,
            "NoTel": self.notel,
        }

        return person_list