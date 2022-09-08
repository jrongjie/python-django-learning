# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# f-string is for formating data, it basically substitutes known variables with their value

## create function -- starts with defining the function
def greet(name):
    print(f'Yo {name}')     

greet('Jen')

## since we cant leave a parameter blank we can add defaults for when there's no known value to a variable
def bye(name = 'whatsyourface'): 
    print(f'See ya {name}')     

bye()

## return values
def getSum (num1, num2):
    total = num1 + num2
    return total

num = getSum(2,3)
print(num)
print(getSum(3,4))  # alternative way of writing

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
#func = lambda [parameters] : [expression/body of function]

print(getSum(5,6))