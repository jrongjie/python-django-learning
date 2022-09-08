# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1             # int -- no semicolons or declairation
y = 2.9           # float
name = 'Jen'      # str, can use single/double quotes
is_cool = True    # bool, must be capital T/F

# multi assignment
x, y, name, is_cool = (1, 2.5, 'Jen', True)

# basic math
a = x + y

# casting
x = str(x)
y = int(y)    # changing a float does not round to the nearest number, just uses the last whole digit
z = float(y)  # since the number changed to an int, when it goes back to being a float it resets to 2.0 

print (type(z), z) # python 2 uses ' ', python 3 uses ()
