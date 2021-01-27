current_users = ['Monkeyman32', 'SomethingWandom', 'catzrfluffy43', 'somethingdeliberate', 'TheKittenSleeping636']
#Yes, there's a lot of cat usernames

new_users = ['Monkeyman321', 'SomethingWandom', 'toontownrewritten3213', 'fnaffanboy5151523', 'shishkebab4124']

current_users_lowercase = ['monkeyman32', 'somethingwandom', 'catzrfluffy43', 'somethingdeliberate', 'thekittensleeping636']


for username in new_users: # Any username in the new_users list
    if username.lower() in current_users_lowercase: # Case insensitive
        print(f"{username} will not work, you will need to enter in a new username.")
    else:
        print("This username is available.")

