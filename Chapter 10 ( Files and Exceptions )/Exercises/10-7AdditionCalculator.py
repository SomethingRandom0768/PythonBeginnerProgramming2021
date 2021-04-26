print("Please enter two numbers.")

first_num_failed = True
second_num_failed = True

while first_num_failed == True:
    try:
        first_num = int(input("First number: "))
        first_num_failed = False
    except ValueError:
        print("Please enter in a valid number next time.")


while second_num_failed == True:
    try:
        second_num = input("Second number: ")
        second_num_failed = False
    except ValueError:
        print("Please enter in a valid number next time.")
