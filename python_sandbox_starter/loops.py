# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
pets = ['dog', 'cat', 'fish', 'bird']

## simple for loop
'''for pet in pets:
    print(f'Possible Pets: {pet}')'''

## break loop -- stops the loop at the first instance
for pet in pets:
    if pet == 'cat':
        break
    print(f'hypoallergetic Pets: {pet}')

## continue loop -- skips the loop at the instance
for pet in pets:
    if pet == 'cat':
        continue
    print(f'scary Pets: {pet}')

## range loop
for i in range(len(pets)):
    print(pets[i])

## custom range -- starts at first value and then up to the last value but doesn't include the last value
for i in range(0, 9):
    print(f'Numer: {i}')


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'count: {count}')
    count +=1