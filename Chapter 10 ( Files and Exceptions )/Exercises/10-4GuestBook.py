name_counter = 0
is_taking_names = True

while is_taking_names == True:
    name = input("Please enter the guest's name (enter no to leave): ")
    name_counter += 1
    with open('guests_list.txt', 'a') as file_object:
        file_object.write(f"{name}\n")
        file_object.write(f"\m{name} is #{name_counter} on the list.")
