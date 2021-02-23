# Using code from 9-3
class User():
    """Model of a person's user profile"""
    def __init__( self, first_name, last_name, age, username, password, ):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.username = username
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Describes all of the user's information"""
        print(f"The user's name is {self.firstname} {self.lastname}\nThey are {self.age} years old\n"
              f"Their username is {self.username} and their password is {self.password}")

    def greet_user(self):
        """Prints out a greeting to the user"""
        print(f"Welcome {self.username}!")

    def increment_login_attempts(self):
        """Increments the amount o login attempts by one"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the amount of login attempts"""
        self.login_attempts = 0


test_user = User("Monkey", "Exists", 15, "thismonkeyistesting321", "testaccount321")
test_user.increment_login_attempts()
test_user.increment_login_attempts()
print(test_user.login_attempts)

test_user.reset_login_attempts()
print(test_user.login_attempts)