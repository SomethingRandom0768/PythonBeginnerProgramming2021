
class Restaurant:
    """Model of a restaurant"""
    def __init__(self, name, type_cuisine):
        self.name = name
        self.type_cuisine = type_cuisine

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and the type of cuisine is {self.type_cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is opening! ")

first_restauraunt = Restaurant("The Cat Cafe", "Fish")
second_restaurant = Restaurant("The Dog Cafe", "Meat") # I wonder, do dog cafes exist? Would be nice.
# One does exist in Los Angeles as far as I read, wonder if there's one here in Texas :]
third_restaurant = Restaurant("The Monkey Barz", "Bananas") # The only drink they serve is banana smoothies
