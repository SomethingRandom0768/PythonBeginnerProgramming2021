
usernames = ['cookiemonster321', 'SomethingRandom', 'SomethingDeliberate', 'KittenMan3135525', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")