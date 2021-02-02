favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

list_of_people = ['sarah', 'monkey', 'shishkebab', 'phil']

for name in list_of_people:
    if name in favorite_languages: # Automatically defaults to keys so I'm good on adding .keys() to the end.
        print(f"\nThank you for submitting an answer, { name.title() }!")
    else:
        print(f"\nHey {name.title()}! Could you please answer our poll? Thanks!")