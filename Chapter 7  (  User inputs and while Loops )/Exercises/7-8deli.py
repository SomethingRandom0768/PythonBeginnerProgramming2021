sandwich_orders = ['Baura', 'Bologna', 'Caviar', 'American sub', 'Bagel toast']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made you {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
    del sandwich # Pop wasn't being nice so I just ended up deleting the sandwich being created.

print("\nThis is the list of sandwiches that were created:\n")
for created_sandwich in finished_sandwiches:
    print(f"{created_sandwich}")


