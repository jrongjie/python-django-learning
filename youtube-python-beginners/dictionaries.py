# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

## create dict
person = {
    'name' : 'Jen',
    'age' : 24,
    'gender' : 'F'
}

print(person, type(person))

## use constructor
human = dict(name='Jenny', color='red')
print(human, type(human))


## get value
print(person['name'])
print(person.get('age'))

## add key/value
person['word'] = 'bro'
print(person)

## get dict keys
print(person.keys())

## get dict items -- will return --> dict_items([('name', 'Jen'), ('age', 24), ('gender', 'F'), ('word', 'bro')])
print(person.items())

## copy dict -- similar to js' spread operator, get all the values of an object and add to it
person2 = person.copy()
person2['life'] = 'good'
print(person2)

## remove item
del(person['age'])
person.pop('word')
print(person)

## clear -- will return empty brackets
#person.clear()
print(person)

## get length -- returns how many key/value pairs exist
print(len(person))

## liat of dict
people = [
    {'name': 'Jen', 'id': 3},
    {'name': 'Jenny', 'id': 5}
]
print(people[1]['name'])

# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
