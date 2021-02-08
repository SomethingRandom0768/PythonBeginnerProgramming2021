
def get_formatted_name(first_name, last_name):
    """"Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    # Adding a break statement of my own because I don't want to deal with an infinite loop
    # Turns out there was one in the example right after I wrote it  but I'll leave mine in >:}
    answer = input("Would you like to enter another name? (yes/no) ")

    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("\nPlease enter a valid answer. (yes/no)")