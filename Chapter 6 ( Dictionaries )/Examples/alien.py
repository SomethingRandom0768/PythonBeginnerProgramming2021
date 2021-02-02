# Accessing Values in a Dictionary

alien_o = {'color': 'green', 'points': 5}
print(alien_o['color'])

new_points = alien_o['points']
print(f"You just earned {new_points} points!")


# Adding New Key - Value Pairs
alien_o = {'color': 'green', 'points': 5}
print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

# Starting with an empty dictionary
alien_o = {}

alien_o['color'] = 'green'
alien_o['points'] = 5

print(alien_o)

# Modifying Values in a Dictionary
alien_o = {'color': 'green'}
print(f"The alien is {alien_o['color'] }.")


alien_o['color'] = "yellow"
print(f"The alien is now {alien_o['color']}.")

# Removing key pairs

alien_o = {'color': 'green', 'points': 5}
print(alien_o)

del alien_o['points']
print(alien_o)

