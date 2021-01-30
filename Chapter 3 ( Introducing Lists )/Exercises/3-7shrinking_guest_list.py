guest_list = ["shishkebab", "SomethingDeliberate", "SomethingRandom"]

print("It turns out that we've found a bigger table so we can invite more people!\n")

guest_list.insert(0, "Kitty")
guest_list.insert(1, "Oh Deer")
guest_list.append("Pusheen")

message1 = f"Hi {guest_list[0]}, would you like to come for dinner tonight?"
message2 = f"Hi {guest_list[1]}, would you like to come for dinner tonight?"
message3 = f"Hi {guest_list[2]}, would you like to come for dinner tonight?"
message4 = f"Hi {guest_list[3]}, would you like to come for dinner tonight?"
message5 = f"Hi {guest_list[4]}, would you like to come for dinner tonight?"
message6 = f"Hi {guest_list[5]}, would you like to come for dinner tonight?"

print(message1) # Pretty much a copy and paste
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

# Using the same program from 3-6 above

print("\nOh no! The table won't arrive in time so we'll have to remove a few people :( \n")

# We've got 6 people in the list right now, so we should remove 4 of them

first_person = guest_list.pop(0)
second_person = guest_list.pop(0)
third_person = guest_list.pop(0)
fourth_person = guest_list.pop(0)


goodbye1 = f"Sorry {first_person}, but you can't come :( Come back whenever we get the bigger table!"
goodbye2 = f"Sorry {second_person}, but you can't come :( Come back whenever we get the bigger table!"
goodbye3 = f"Sorry {third_person}, but you can't come :( Come back whenever we get the bigger table!"
goodbye4 = f"Sorry {fourth_person}, but you can't come :( Come back whenever we get the bigger table!\n"

print(goodbye1) # Printing all the sorry messages
print(goodbye2)
print(goodbye3)
print(goodbye4)

coming1 = f"{guest_list[0]}, you can come since there's only 2 spots left!"
coming2 = f"{guest_list[1]}, you can come since there's only 2 spots left!"

print(coming1)
print(coming2)

del guest_list[0] # Deleting the two people that are left in the list.
del guest_list[0]

