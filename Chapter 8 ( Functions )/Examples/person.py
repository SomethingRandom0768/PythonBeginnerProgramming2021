

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name,
              'last': last_name}
    if age:
        person['age'] = age # You basically add a new key and value here.

    return person

musician = build_person('jimi', 'hendrix', age=27) # I'm not sure if I should feel bad cause I don't know who Jimi Hendrix is.
print(musician)