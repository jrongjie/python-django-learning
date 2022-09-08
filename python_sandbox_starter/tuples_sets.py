# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
## create tuple
veggies = ('corn', 'peas', 'carrots')
vegetables = tuple(('corn', 'peas', 'carrots'))

print(veggies, vegetables)

## single value needs a trailing comma, or it turns into a str
fruits = ('grapes',)
print(fruits, type(fruits))

## get value
print(veggies[1])

## can't change value
##veggies[0] = 'asparagus'
print(veggies[0])

## delete tuple
#del fruits
print(fruits) # will throw an undefined since it's now deleted

## get length
print(len(veggies))


# A Set is a collection which is unordered and unindexed. No duplicate members.

## create set
meats = {'cow', 'chicken', 'pig'}

## check if in set -- returns T/F
print('pig' in meats)

## add to set
meats.add('goat')
print(meats)

## remove item from set
meats.remove('cow')
print(meats)

## add dup
meats.add('pig')
print(meats) # wont throw error, just not gonna do anything

## clear set -- will return empty set, different from deleting
meats.clear()
print(meats)

## delete -- will throw an undefined 
del meats
print(meats)
