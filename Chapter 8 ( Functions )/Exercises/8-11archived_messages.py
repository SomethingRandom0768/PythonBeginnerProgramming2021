# This is basically the same as 8-10, except for the fact that when I'm calling the function, I'm
# using a copy of the list.

def send_messages(message_list, finished_messages):
    """Moves messages over to a new list of sent messages"""
    while message_list: # While the first list isn't empty.
        message = message_list.pop()
        print(f"Printing message: {message}")
        finished_messages.append((message))

short_messages = ['Hi there!', "How ya doing?!", 'Yo.', 'I want to eat peanut butter cookies.']

sent_messages = []

send_messages(short_messages[:], sent_messages)

# You can tell this is a copy because when I start printing out the lists, they're both exactly the same
# because I never took out anything FROM the original list and instead used a copy.

print(short_messages) # Checking the lists to see if they were moved correctly
print(sent_messages)


