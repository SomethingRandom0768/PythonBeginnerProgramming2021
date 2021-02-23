
class User:
    """Model of a person's user profile"""
    def __init__(self, first_name, last_name, age, username):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.username = username
    def describe_user(self):
        """Describes all of the user's information"""
        print(f"The user's name is {self.firstname} {self.lastname}\nThey are {self.age} years old\n"
              f"Their username is {self.username}\n")

    def greet_user(self):
        """Prints out a greeting to the user"""
        print(f"Welcome {self.username}!")

first_user = User("Monkey", "Dinko", 31, "asecret14414415266t525r23r1")
first_user.describe_user()
first_user.greet_user()

second_user = User("Lol", "lol", 31, "NotReal321")
second_user.describe_user()
second_user.greet_user()

third_user = User("Max", "Donovan", 19, "CouldBeRealI'mNotSure3123")
third_user.describe_user()
third_user.greet_user()