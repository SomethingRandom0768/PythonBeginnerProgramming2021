# Reusing code from 9-7.

# The user class
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

# The privilege class
class Privileges:
    def __init__(self, privileges=["can ban users", "can kick users", "can ban users", "can access secret channels"]):
        self.privilegeList = privileges

    def show_privileges(self):
        for privilege in self.privilegeList:
            print(privilege)

# The admin class
class Admin(User):

    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.privileges = Privileges()

AdminTwo = Admin("The", "Cat", 29, "TheCatMan321")

AdminTwo.privileges.show_privileges()