class Restaurant:
    """Model of a restaurant"""

    def __init__(self, name, type_cuisine):
        self.name = name
        self.type_cuisine = type_cuisine

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and the type of cuisine is {self.type_cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is opening! ")

restaurant = Restaurant("Monkey Barz", "Banana")

restaurant.describe_restaurant()
restaurant.open_restaurant()