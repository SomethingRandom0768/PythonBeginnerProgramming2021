# Uses cats.txt and dogs.txt

try:
    with open('cats.txt') as file_object:
        cats = file_object.readlines()
except FileNotFoundError:
    print("Cannot find cats.txt")

try:
    with open('dogs.txt') as file_object:
        dogs = file_object.readlines()
except FileNotFoundError:
    print("Cannot find dogs.txt")


print("Cat names:")
for cat in cats:
    print(f"{cat.strip()}")

print("\nDog names:")
for dog in dogs:
    print(f"{dog.strip()}")