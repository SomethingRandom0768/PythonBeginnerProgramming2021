# Used for 9-12

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