# Reusing a list from 4-2 but just adding more animals to fit the exercise
animals = ['dog', 'cat', 'ferret', 'jaguars', 'lions', 'boars', 'pigs']

first_three = animals[ : 3 ]
middle_three = animals[ 3 : 4]
last_three = animals[-3 : ]

# print statements
print(f"The first three items in the list are: {first_three}")
print(f"Three items from the middle of the list are: {middle_three}")
print(f"The last three items in the list are: {last_three}")
