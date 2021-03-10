### I have left all the print statements uncommented!
### You may wish to go through and comment out parts
### that you aren't currently looking at
### Enjoy :)

# This is a string!
name = 'James'

# Strings need to have speech marks either side of them
# to make them into a string!

# Strings need to have the same type of speech marks either
# side, I use single quotes, but double speech marks also work well.


## Multiline strings can also be created using triple quotes

shopping_list = '''
1. Cheese
2. Ham
3. Eggs
'''

print(shopping_list)


# Special characters can be added to strings,
# these can add new lines and tab spaces
# backslash + n is for a new line!
# backslash + t is for a tab space


# Adding a linebreak between each word
print('One\nTwo\nThree')

# Adding some tabbed spaces
print('Ten\tTwenty\t\tThirty')

# I will be adding some line breaks in this file
# to break up the sections


print('\n\n')
#### Indexing ####
# Each position in the string is unique,
# and this is called its Index. Indices are accessed
# by using square brackets

# Strings are 'zero-indexed' meaning we count from 0
# So an index of 0, is the first letter
print(name[0])


# second letter
print(name[1])

# Passing an integer in as the index
pos = 4
print(name[pos])

# This will cause an IndexError as no index of 8 exists!
# print(name[8])

# Accessing the last element
print(name[-1])

print('\n\n')
#### Slicing ####

# Slicing is accessing a portion of the string
# instead of just one element
# Slicing can be done using 3 commands inside
# the square brackets
# [start: stop: step]

# start: which position to start at
# stop: which position to stop at
# step: how many positions to jump over

city = 'Manchester'

# Elements 1 up until 4
print(city[1:4])

# All elements up until position 4
print(city[:5])


# All elements from position 3
print(city[3:])

# Elements 1 up until 8, in steps of 2
print(city[1:8:2])

# All elements in steps of 2
print(city[::2])

# The entire string, in reverse!
print(city[::-1])

# From the start, until position 8, in 3's
print(city[:8:3])

print('\n\n')
#### Joining Strings Together ####

# Strings can be joined together,
# this is called 'Concatenation'

string1 = 'abc'
string2 = 'def'
new_string = string1 + string2
print(new_string)

another_new_string = new_string + 'ghi'

print(another_new_string)

print('\n\n')
#### String Methods ####

# Calling the dir(directory) function
# shows all the methods you can do with a string.
# You can pass almost anything into the dir() function!

print(dir(str))


# A method is an action that can be performed on a variable
# Each type (str, int, bool etc..) has its own set of methods
# String methods don't 'change' the original variable
# instead, they return new data!

drink = 'milk shake'

# Returning the uppercase version to a new variable
drink_uppered = drink.upper()
print(drink_uppered)


# Returning the titlecase version to a new variable
# (upper cases the first letter of each word)
drink_titled = drink.title()
print(drink_titled)


# Returning a lowercased version to a new variable
# string is already lowercase however!
drink_lowered = drink.lower()
print(drink_lowered)

# Returning a capitalized version to a new variable
# Only capitalizes the first letter of the entire string
# not each individual word!
drink_capitalized = drink.capitalize()
print(drink_capitalized)
