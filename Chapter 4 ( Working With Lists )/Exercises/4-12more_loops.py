# Using the list from foods.py over in examples

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[ : ]

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)