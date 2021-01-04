motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati" # Changes the first index of the list ( honda ) to ducati
print(motorcycles)

motorcycles[0] = "honda" # Setting it back to the original honda it was
print(motorcycles)

motorcycles.append('ducati') # Adding ducati to the end of the list
print(motorcycles)

motorcycles = [] # Creating a new list to use

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles = ['honda','yamaha', 'suzuki']

motorcycles.insert(0, 'ducati') # Replace whatever's at index 0 with 'ducati' and push anything ahead forward
print(motorcycles)

del motorcycles[0] # deletes the ducati we just added since that's at index 0
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # Uses the pop method to get the last index and now you can use that data
print(motorcycles)
print(popped_motorcycle) # Since the popped_motorcycle was popped, it can be used.and it prints out "suzuki"

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# You can pop from any position by including the index of a position
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # searches for whatever's inside too_expensive and then removes it from the list
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.") # Using the too_expensive variable in a print statement

