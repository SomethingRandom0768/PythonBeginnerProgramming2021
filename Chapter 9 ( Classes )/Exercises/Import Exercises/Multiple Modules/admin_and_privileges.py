# Used for 9-12
from onlyUser import User


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