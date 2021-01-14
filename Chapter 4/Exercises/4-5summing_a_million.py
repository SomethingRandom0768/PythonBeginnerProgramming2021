million_numbers = []

for value in range(0, 1000001):
    million_numbers.append(value)


minimum = min(million_numbers)
maximum = max(million_numbers)
list_sum = sum(million_numbers)

print(f"The minimum is {minimum}\nThe maximum is {maximum}\nThe sum is {list_sum}")