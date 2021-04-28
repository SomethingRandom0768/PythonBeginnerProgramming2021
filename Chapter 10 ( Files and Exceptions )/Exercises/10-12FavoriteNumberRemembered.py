import json


def get_new_number():
    """Allows the user to enter in a new favorite number"""
    favorite_num = input("What's your favorite number? ")
    
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_num, f)
    return favorite_num

def get_stored_number():
    """Allows the user to load up an already saved favorite number"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number



def greet_the_user():
    favorite_number = get_stored_number()
    if favorite_number:
       print(f"I know your favorite number, it's {favorite_number}")
    else:
        favorite_number = get_new_number()
        print(f"We'll remember you when you come back, {favorite_number}!")

greet_the_user()