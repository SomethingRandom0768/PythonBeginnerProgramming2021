def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)
# Man, I'm looking back at that for statement and I remember thinking it was hard to use a for loop
# on lists. Time sure does fly.

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
