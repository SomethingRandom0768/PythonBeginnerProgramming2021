# Apparently there's 2 types of arguments: positional and keyword. WHOOOOOOOOOOOOOOOOOO

# Basically, psoitinoal arguments are like a machine. It'll put stuff in on the left first, then the right.

def describe_pet(animal_type, pet_name): # In this case, the first paraaeter put into the call becomes animal_type
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster','harry') # YOU'RE A WIZARD HARRY
describe_pet('dog', 'willie')  # dog goes to animal_type, willie goes to pet_name

# Keyword arguments, now THIS is new to me.

describe_pet(animal_type='hamster', pet_name='harry') # Basically you assign the values in the function.
describe_pet(pet_name='harry', animal_type='hamster') # It don't matter where it goes, because Python knows
# to rearrange the arguments you put in to the function's original parameters. Really really neat idea.

def describe_pet2(pet_name, animal_type='dog'): # This is a default parameter, so the person reading this
    # is automatically going to assume this function is being used for dogs primarily unless written otherwise.
    """Display information about a pet, AGAIN."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
# When creating a default parameter function, always do the NON defaults before. Just think of it as
# asking for what type of ice cream you want. The default is that there's always going to be a cone under ^-^

describe_pet2(pet_name='willie')

# Using a Keyword argument allows you to override the default value
describe_pet2(pet_name='harry', animal_type='hamster')