filename ="reasonsToLikeProgramming.txt"
can_enter_reasons = True

while can_enter_reasons:
    reason = input("Why do you like programmming?")
    
    with open(filename, 'a') as file_object:
        file_object.append(reason)
