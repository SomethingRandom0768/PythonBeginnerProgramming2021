# Uses cats.txt and dogs.txt. Only difference between this and 10-8 is that I'm silently passing the errors.

try:
    with open('cats.txt') as file_object:
        cats = file_object.readlines()
except FileNotFoundError:
    pass

try:
    with open('dogs.txt') as file_object:
        dogs = file_object.readlines()
except FileNotFoundError:
    pass


print("Cat names:")
for cat in cats:
    print(f"{cat.strip()}")

print("\nDog names:")
for dog in dogs:
    print(f"{dog.strip()}")