# Using the same list from last exercise
sandwich_orders = ['Baura', 'pastrami', 'Bologna', 'Caviar', 'pastrami','American sub', 'pastrami', 'Bagel toast']

finished_sandwiches = []

print("Oh no! The deli has run out of pastrami :( we have to cancel all pastrami orders, sorry!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"A {sandwich} sandwich was made")
    finished_sandwiches.append(sandwich)
    del sandwich # Pop wasn't being nice so I just ended up deleting the sandwich being created.

print("\nThis is a list of sandwiches that were created:\n")
for created_sandwich in finished_sandwiches:
    print(f"{created_sandwich}")

