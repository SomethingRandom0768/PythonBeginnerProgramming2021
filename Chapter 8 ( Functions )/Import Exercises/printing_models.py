import printing_functions as pf

# Start with some designs that need to be printed.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
# The functions below were commented out for 8-15, printing functions.
# These functions were moved over there and the file was imported here
#def print_models(unprinted_designs, completed_models): # Okay, documentation is awesome. No clue it showed that.
#    """
#    Simpulate printing each design, until none are left.
#    Move each design to completed_models after printing
#    :param unprinted_designs:
#    :param completed_models:
#    :return:
#    """
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
#        print(f"Printing model: {current_design}")
#        completed_models.append(current_design)

#def show_completed_models(completed_models):
#    """Show all the models that were printed."""
#    print("\nThe following models have been printed:")
#    for completed_model in completed_models:
#        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)