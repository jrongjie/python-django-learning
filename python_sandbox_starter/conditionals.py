# If/ Else conditions are used to decide to do something based on something being true or false

x = 20
y = 40


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
## simple if
if x > y :
    print(f'{x} is better than {y}')

## if else
if x > y :
    print(f'{x} is better than {y}')
else:
    print(f'{y} is better than {x}')

## elif -- requires a condition set to be the same ==
a = 5
b = 5

if x > y :
    print(f'{a} is worse than {b}')
elif x == y:
    print(f'{a} is the same as {b}')
else:
    print(f'{a} is better than {b}')

## nested if
if x > 2:
    if x <=20:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements
## and -- both have to be true
if x > 4 and x <= 20:
    print(f'{x} is greater than 4 and less than or equal to 10')

## or -- either have to be true
if x > 4 or x <= 20:
    print(f'{x} is greater than 6 and less than or equal to 10')

## not -- either have to be true
if not(x == y):
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object # will return a T/F
me = 2
ids = [1,2,3,4,5]
if me in ids:
    print(me in ids)

you = 10
if you not in ids:
    print(you not in ids)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location: # will return T/F
c = 6
d = 7
if c is d:
    print(c is d)

if c is not d:
    print(c is not d)