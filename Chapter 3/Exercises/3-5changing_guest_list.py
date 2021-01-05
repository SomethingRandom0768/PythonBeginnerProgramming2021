guest_list = ["shishkebab", "SomethingDeliberate", "SomethingRandom"]
# Using the same list from 3-4

announcement = f"Unfortunately, {guest_list[0]} can't make it to the party so we get to invite another person!"
print(announcement)

guest_list[0] = "monkey"

message1 = f"Hi {guest_list[0]}, would you like to come for dinner tonight?"
message2 = f"Hi {guest_list[1]}, would you like to come for dinner tonight?"
message3 = f"Hi {guest_list[2]}, would you like to come for dinner tonight?"

print(message1) # Pretty much a copy and paste
print(message2)
print(message3)