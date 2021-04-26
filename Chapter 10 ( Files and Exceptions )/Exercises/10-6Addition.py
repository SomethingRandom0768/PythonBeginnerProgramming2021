print("Please enter two numbers.")

try:
    first_num = input("First number: ")
except ValueError:
    print("Please enter in a valid number next time.")

try:
    second_num = input("Second number: ")
except ValueError:
    print("Please enter in a valid number next time.")
