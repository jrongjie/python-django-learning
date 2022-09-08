# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Jen'
age = 24

# concatenate -- can only concate str not ints
print('Yo, I\'m ' + name + ' and I have ' + str(age) + ' years.')

# String Formatting
## arguments by position
print('Yo, I\'m {name} and I am {age}'.format(name=name, age =age))

## F-srings -- only for python 3.6+, similar to JS template literals
print(f'Yooo, {name} here, I got {age} years')

# String Methods
s = 'hello world'

## capitalize str -- needs to have () at the end since it's a method and therefore a type of function
print(s.capitalize()) 

## uppercase
print(s.upper())
## lowercase
print(s.lower())
## swapcase
print(s.swapcase())

# get length -- function can be used on all data types
print(len(s)) 
## replace
print(s.replace('hello', 'see ya'))
## count -- counts the number of times the sub appears in the string
sub = 'h'
print(s.count(sub))

## starts with -- returns T/F based on how it starts
print(s.startswith('hello'))
## ends with -- returns T/F based on how it ends
print(s.endswith('d'))
## split into a list -- basically just makes an array
print(s.split())

## find position -- looks for the position of the first occurance
print(s.find('r'))

## is all alphanumeric -- returns T/F
print(s.isalnum())
## is all alphabetic -- returns T/F
print(s.isalpha())
## is all numeric -- returns T/F
print(s.isnumeric())
### alpha/numeric will return False because of spaces
