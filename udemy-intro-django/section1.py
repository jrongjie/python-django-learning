# 1.4 The python IDLE
# print ('hello world')

### 1.6 Python List - zero based ###
sodas = ['coke', 'sprite', 'rootbeer', 'pepsi']
#print(sodas[1])

#redeclare a value
sodas[1] = 'ginger ale'
#print(sodas[1])

#add to list
sodas.append('canada dry')
#print(sodas)

#remove value from list
del sodas[4]
#print(sodas)

### 1.7 Python Tuples - immmutable lists ###
pets = ('dog', 'cat', 'fish', 'bird')

### 1.9 Your first Python Program ###
#print('How much food ya got?')
amount = input()
#print('Mmm ' +amount+ ' pieces is\'t enough for me and you to eat')

### 1.10 Generating Random Numbers ###
import random
for i in range(1,200): #this errors out, not written correctly
    print(random.randint(1,200))

### 1.11 Number Guessing Game ###
