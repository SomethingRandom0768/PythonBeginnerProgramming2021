# Set the default shirt size to "large" and the default message is "I love Python"
def make_shirt(size='large', message="I love Python"):
    print(f"The size of the shirt is {size.title()} and the text is '{message}'")

make_shirt() # No need to type in anything considering they are the defaults.

make_shirt(size="medium")

# Using keyword arguments to bypass the default and add in our own values
make_shirt(size="Extra large", message="This message was coded in.")



