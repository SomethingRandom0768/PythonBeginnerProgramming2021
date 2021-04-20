# No, I am not learning C right now lOL....maybe later perhaps?

file = 'learning_python.txt'

with open(file) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').strip())


