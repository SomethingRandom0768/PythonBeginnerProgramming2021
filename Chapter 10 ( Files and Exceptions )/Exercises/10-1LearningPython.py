# First option: reading the entire file and printing it out.
file = 'learning_python'

with open(file) as file_object:
    lines = file_object.readlines()

print(lines)

# Second option: Reading each line from the list and printing it out.

with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Third option: Reading each line, appending to a list, and then printing out that list.

with open(file) as file_object:
    lines = file_object.readlines()

words = [] # Empty list

for line in lines:
    words.append(line.strip()) # Append here.

print(words)