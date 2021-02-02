# Difference between this and 6-3 is that I created a for loop
# and I added 5 more terms
words = {'List': 'Structure containing objects, strings, or numbers',
         'Conditional test': 'Simple expression to test whether something is equal or not',
         'Pop method': 'Method used to remove the last index of a list but allow you to use that value',
         'elif': 'else - if, used if the first conditional test fails in an if statement, can be followed by else',
         'Operators': 'Symbols that represent operations, math operators are an example',
         'Set': 'Basically a list but prevents any duplicates',  # first new one
         '.values()': 'Method that returns a list of values in a dictionary',
         '.keys()': 'Method that returns a list of keys in a dictionary, also default when using a for loop.',
         'Tuple': 'An immutable list.',
         'else': 'A catch all part of an if statement if both elif and the original conditional test fail'
         }

for k, v in words.items():
    print(f"\nThe word is {k}")
    print(f"It's definition is '{v}' ") # Used single quotes to wrap around the value to look nicer.