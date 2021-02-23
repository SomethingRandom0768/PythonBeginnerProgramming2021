# This exercises uses code from 9-1

class Restaurant:
    """Model of a restaurant"""

    def __init__(self, name, type_cuisine):
        self.name = name
        self.type_cuisine = type_cuisine
        self.number_served = 0 # The main focus of this exercise


    def describe_restaurant(self):
        """Prints out a statement with the restaurant's name as well as the type of cuisine it serves."""
        print(f"The name of the restaurant is {self.name} and the type of cuisine is {self.type_cuisine}")

    def open_restaurant(self):
        """Prints out a message stating that the restaurant is opening."""
        print(f"{self.name} is opening! ")

    def set_number_served(self, new_served):
        """Changes the numbeer served attribute to the parameter given"""
        self.number_served = new_served

    def increment_number_served(self, servedToAdd):
        self.number_served += servedToAdd



restaurant = Restaurant("Monkey Barz", "Banana")

print(f"The number served is {restaurant.number_served}")
restaurant.number_served = 15 # Changing through dot notation
print(f"The number served now is {restaurant.number_served} ")

restaurant.set_number_served(15) # utilizes the method to change the number served in the restaurant.
print(f"The number served now is {restaurant.number_served}")


