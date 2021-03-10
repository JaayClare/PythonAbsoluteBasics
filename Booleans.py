### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.

### Enjoy :)

# A Boolean (or bool) can have two possible values, True or False

# Every variable in Python has a boolean representation. I'll cover this with Strings, ints and floats

# any non-empty string is True
food = 'Cheese'
# An empty string is False (it has no value!)
food_two = ''

# This shows True then False
print(bool(food), bool(food_two))


# Any float/integer that is 0, or 0.0 if False, otherwise its True!
g_int= 0
h_int = 10
# This shows False then True
print(bool(g_int), bool(h_int))

g_float= 0.0
h_float = 0.10
# This shows False then True
print(bool(g_float), bool(h_float))


# We see Booleans in if statements, while loops and more.
# for example, lets look at the following if statement..
# The if statement on line 12 needs to be 'True' for the print statement below to run.
# So Python will ask 'Is X greater than 5?', and if so, the situation is True!

x = 10

if x > 5:
  print(x, 'is greater than 5!')
else:
  print(x, 'is not greater than 5')

# We can also check this by running the following code

print(x > 5) # This will print 'True' because x is greater than 5.


#### Evaluating Statements with Print ####

# Print is obviously useful for showing outputs on the screen, but it can also evaluate a statement and show True/False!


# This will evaluate that 10 is larger than 2, so it will show True!
print(10 > 2)

# True
print(10 == 10)

# False
print(10 != 10)


# False
a = 'x'
b = 'xy'
print(a == b)

print('\n\n')
#### Boolean Logic ####

# We can use 3 additional words to evaluate more complex situations
# and (Looks at the statement either side of the 'and' and it requires both to be True)
# or (Looks at the statement either side of the 'or' and it requires either to be True)
# not (Flips a True into a False, and a False into a True)

# For this whole statement to be True, the 'and' requires both sides to be True!
#print( (statement1) and (statement2))

# True! Because both sides are True
print((10 > 5) and (100 == 100))

# True, because the 'or' only requires one side to be True
print((10 == 5) or (100 == 100))

# False, because the left side is False and the 'and' requires both to be True
print((10 == 5) and (100 == 100))

# This would  normally be False
print((10 == 5))

# But lets flip it with a not. This inverts the Boolean
print(not(10 == 5))


# True!
# The left side would have been false, but has been flipped with the Not!
i = 1000
j = 150
print((i > j) and not(10 != 10))


print('\n\n')
#### Interesting use of Booleans in IF statements ####


# If statements look to see if a Boolean condition has been satisfied or not.
# So if we simply say 'if variable:', it will look at the boolean representation of the variable.
# This is useful if you want an IF statment to run if a string contains data or not, because a non-empty string is True


name = 'James'
if name:
    print('Hello!', name)


# lets prove it.. This shows True
print(bool(name))

name = ''
if name:
    print('Hello!', name)
else:
    print('No data in name')

# This shows False
print(bool(name))
