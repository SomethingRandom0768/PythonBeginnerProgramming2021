group_number = input("How many people are in your table group? ")
group_number = int(group_number)

if group_number > 8:
    print("Unfortunately, you'll have to wait for another table to become vacant.")
else:
    print("Your table is ready.")
