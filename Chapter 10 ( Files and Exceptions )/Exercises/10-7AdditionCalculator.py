print("Please enter in two numbers to add. (Type '1' to quit.)")

while True:
        try:
            first_num = int(input("First number: "))
            if first_num == 1:
                break
        except ValueError:
            print("Please try again.")
            first_num = int(input("First number: "))
            if first_num == 1:
                break
        try:
            second_num = int(input("Second number: "))
            if second_num == 1:
                break
        except ValueError:
            print("Please try again.")
            second_num = int(input("Second number: "))
            if second_num == 1:
                break
        third_num = first_num + second_num
        print(f"The sum of {first_num} and {second_num} is {third_num}")