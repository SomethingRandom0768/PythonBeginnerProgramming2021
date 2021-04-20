

name = input("Please enter your name: ")

with open('guest.txt', 'a') as file_object:
    file_object.write(name)