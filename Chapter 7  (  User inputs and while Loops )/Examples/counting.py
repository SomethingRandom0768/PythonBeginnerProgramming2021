current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # Basically what this does is if this is true, then "continue" the loop and disregard the code below.
    print(current_number)