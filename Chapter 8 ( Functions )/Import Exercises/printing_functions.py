# This is actually 8 - 15 but I had to change the name or else
# the import statement would disagree with me and start throwing errors

def print_models(unprinted_designs, completed_models): # Okay, documentation is awesome. No clue it showed that.
    """
    Simpulate printing each design, until none are left.
    Move each design to completed_models after printing
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)