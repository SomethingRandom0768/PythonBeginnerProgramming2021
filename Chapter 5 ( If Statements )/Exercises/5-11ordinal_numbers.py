numbers = range(1, 101) # Added my own spin to this exercise, instead of 1 - 9, why not 1 - 100?

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")