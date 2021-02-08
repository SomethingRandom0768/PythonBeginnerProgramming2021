
def get_formatted_name(first_name, last_name, middle_name=''): # default value for a middle name is ''
    """Return a full name, neatly formatted."""
    if middle_name: # If middle_name has something, THEN print out {middle_name}
        full_name = f"{first_name} {middle_name} {last_name}"
    else: # If not, don't put it in there.
        full_name = f"{first_name} {last_name}"
    return full_name.title() # Returns a full name with title() method applied

musician = get_formatted_name('jimi', 'hendrix') # No middle name here so it's only gonna print what's in the else
print(musician)

