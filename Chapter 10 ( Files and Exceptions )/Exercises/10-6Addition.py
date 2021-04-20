print("Please enter in two numbers to add.")

try:
    first_num = int(input("First number: "))
except ValueError:
    print("Please enter a valid number.")
    first_num = int(input("First number: "))
try:
    second_num = int(input("Second number: "))
except ValueError:
    print("Please enter a valid number.")
    second_num = int(input("Second number: "))

third_num = first_num + second_num
print(f"The sum of {first_num} and {second_num} is {third_num}")