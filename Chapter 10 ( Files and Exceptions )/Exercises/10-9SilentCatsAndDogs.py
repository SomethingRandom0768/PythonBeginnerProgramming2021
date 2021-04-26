files = ['dogs.txt', 'cats.txt']

for txt_file in files:
    try:
        with open(txt_file) as f:
            lines = f.readlines()
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        pass