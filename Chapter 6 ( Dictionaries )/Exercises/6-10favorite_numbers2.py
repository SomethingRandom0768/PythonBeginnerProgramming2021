
favorite_numbers = {'r': [12, 6],
                    'c': [9, 3],
                    's': [13, 1],
                    'coo': [6, 8],
                    'e': [9, 2],
                    'd': [5, 8],
                    'f': [25, 1],
                    }
for name, values in favorite_numbers.items():
        print(f"\nThe person {name} likes the numbers below:")
        for value in values:
            print(value)