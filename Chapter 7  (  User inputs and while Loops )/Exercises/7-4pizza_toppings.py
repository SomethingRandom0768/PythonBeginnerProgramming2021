while True:
    topping = input("Hi there! What type of topping would you like in your pizza? ")
    if topping == 'quit':
        print("Quitting the program.")
        break
    else:
        print(f"Adding {topping}")
