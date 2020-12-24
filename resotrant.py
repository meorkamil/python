class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number Served: {self.number_served}")

    def set_number_served(self, update_number):
        self.number_served = update_number

    def increment_number_served(self, number):
        self.number_served += number

    def open_restaurant(self):
        print("--- Restaurant is Open ---")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.falvour = ["Vanilla", "Chocolate", "Banana"]

    def show_flaveour(self):
        for flavours in self.falvour:
            print(flavours)

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        greet = ("Welcome")
        return greet   

    def greet_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"login Attempts: {self.login_attempts}")

class Admin(User):

    def __init__(self, first_name, last_name, age):
        
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
    

class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)



admin = Admin("Kamil", "Sulaiman", 23)
admin.greet_user()
admin.privileges.show_privileges()
# iceCream = IceCreamStand("Ang long", "Western")
# iceCream.show_flaveour()
# restaurant = Restaurant("Ang long", "Western")
# user = User("Kamil", "Sulaiman", 23)
# user.increment_login_attempt()
# user.increment_login_attempt()
# user.increment_login_attempt()
# user.reset_login_attempts()
# print(user.login_attempts)
# restaurant.set_number_served(12)
# restaurant.increment_number_served(2)
# print(restaurant.open_restaurant())
# print(restaurant.describe_restaurant())

