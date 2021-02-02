
words = {'List': 'Structure containing objects, strings, or numbers',
         'Conditional test': 'Simple expression to test whether something is equal or not',
         'Pop method': 'Method used to remove the last index of a list but allow you to use that value',
         'elif': 'else - if, used if the first conditional test fails in an if statement, can be followed by else',
         'Operators' : 'Symbols that represent operations, math operators are an example'
         }
for k, v in words.items():
    print(f"\nThe word is {k}")
    print(f"It's definition is {v}")
print(f"List : { words['List'] } ")
print(f"Conditional test: { words['Conditional test'] }")
print(f"Pop method: { words['Pop method'] } ")
print(f"elif: { words['elif'] }")
print(f"Operators: { words['Operators'] } ")