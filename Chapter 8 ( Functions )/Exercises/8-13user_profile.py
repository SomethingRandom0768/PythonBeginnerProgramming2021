# The exercise is literally use "user_profile.py" and then create your own profile.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('Something', 'Random',
                             location ='texas',
                             field ='computer science',
                             favorite_drink='water')
print(user_profile)