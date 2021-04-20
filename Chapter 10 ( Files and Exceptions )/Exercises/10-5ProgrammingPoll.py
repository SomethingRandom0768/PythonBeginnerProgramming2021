taking_answers = True


while taking_answers:
    reason = input("Why do you like programming? ")
    with open('reasons_for_liking_programming.txt', 'a') as file_object:
        file_object.write('\n' + reason)