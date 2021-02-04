
dream_vacations = {}

while True:
    name = input("\nHi there! What's your name? ")
    place = input("If you could visit one place in the world, where would you want to go? ")

    # Storing into the dream_vacations dictionary, with name as the key and place as the value.
    dream_vacations[name] = place

    answer = input('\nWould you like to let someone else answer? (yes/no) ')
    if answer == 'no':
        break

for name in dream_vacations.keys():
    print(f"{name} wants to go to {dream_vacations[name]}")