# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list -- most common way
num = [1, 2, 3, 4, 5]
milks = ['cow', 'almond', 'oat', 'soy']

# use a constructor -- js-like way
'''
numcon = list((1,2,3,4,5))
print(num, numcon)
'''

# get a value
print(milks[1])

# get length
print(len(milks))

# append -- adds to the end of the list
milks.append('cashew')
print(milks)

# remove
milks.remove('cow')
print(milks)

# insert into position
milks.insert(2, 'rice')
print(milks)

# remove with pop -- specifies a positon
milks.pop(2)
print(milks)

# reverse list
milks.reverse()
print(milks)

# sort -- alpha
milks.sort()
print(milks)

# reverse sort -- alpha
milks.sort(reverse = True)
print(milks)

# change value
milks[0] = 'goat'
print(milks)
