prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break # If the city is the word quit, then break out of the loop.
    else:
        print(f"I'd love to go to {city.title()}!")