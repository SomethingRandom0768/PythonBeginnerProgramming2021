users = {
        'aeinstein': {
                       'first': 'albert',
                        'last': 'einstein',
                        'location': 'princeton',
                    },
#        'mcurie': {
#                        'first': 'marie',
#                        'last': 'curie',
#                        'location': 'paris',
#                 }
}
# Note: the code above does not work propertly so I've had to comment it out :( .

# This stuff burns my eyes o_o it's so weird

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{ user_info['first'] } { user_info['last'] }"
    location = user_info['location']

print(f"\tFull name: { full_name.title() }")
print(f"\tLocation: {location.title()}")
