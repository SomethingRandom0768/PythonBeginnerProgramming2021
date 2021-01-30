cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # The sort() alphebatizes a list. Beware that you can never go back to its original order.
print(cars)

# If you wanted, put reverse=True into the .sort() function's parameters in order to get a reverse alphabetical order



cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print( sorted(cars) ) # Basically, you can use the sorted method to see what it would be like IF you sorted the array.
# It does not affect the actual list, so it could probably be used for testing purposes and such.
# It also has a reverse=True parameter so using it would be like sorted(cars, reverese=True)

print("\nHere is the original list again:")
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() # This only reverses the order, nothing about sorting alphabetically like sort(). It reverses it permanently, but
# do another .reverse() and it'll revert back.
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars) # This returns the length of the list.


