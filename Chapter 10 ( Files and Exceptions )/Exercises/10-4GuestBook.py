filename = 'guestbook.txt'
can_enter_names = True

while can_enter_names:
    name = input("Please enter your name: ")
    print(f"Hello {name}!")
    
    with open(filename, 'a') as file_object:
        file_object.append(name)
