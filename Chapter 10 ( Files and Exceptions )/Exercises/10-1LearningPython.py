
# Reading in the entire file.

with open('learning_python.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

print("Second time.")

# Looping over the file.

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("Third time.")

lines_list = []

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    lines_list.append(line)

print(lines_list)
