# This is actually 8 - 16 but same deal as printing_functions and printing_models

import import_functions # Import the module
from import_functions import sayHello # Import the function from the module
import import_functions as i_f # Import the module with an alias
from import_functions import sayHello as hello # Import the function sayHello from the module and its alias is hello

import_functions.sayHello("Monkey")
sayHello("Luke")
i_f.sayHello("SomethingRandom")
hello("SomethingDeliberate")

