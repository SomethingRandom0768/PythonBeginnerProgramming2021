# Utilizing the Restaurant class from 9-1.
class Restaurant:
    """Model of a restaurant"""

    def __init__(self, name, type_cuisine):
        self.name = name
        self.type_cuisine = type_cuisine

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and the type of cuisine is {self.type_cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is opening! ")

class IceCreamStand(Restaurant):

    def __init__(self, name, type_cuisine, *flavors):
        super().__init__(name, type_cuisine)
        self.flavors = flavors

    def displayFlavors(self):
        for flavor in self.flavors:
            print(flavor)

newIceCreamStand = IceCreamStand("Ice Scream", "Ice Cream", "Vanilla", "Chocolate", "Strawberry")

newIceCreamStand.displayFlavors()
