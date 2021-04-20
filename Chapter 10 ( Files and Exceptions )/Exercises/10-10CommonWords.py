with open('flymetothemoon.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.count('adore'))