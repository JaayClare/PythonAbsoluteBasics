### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.

### Enjoy :)



# This is a string!
name = 'James'

# Strings need to have speech marks either side of them to make them into a string!

# Strings need to have the same type of speech marks either side, I use single quotes, but double speech marks also work well.


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

# Slicing is accessing a portion of the string instead of just one element
# Slicing can be done using 3 commands inside the square brackets
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

# Strings can be joined together, this is called 'Concatenation'

string1 = 'abc'
string2 = 'def'
new_string = string1 + string2
print(new_string)

another_new_string = new_string + 'ghi'

print(another_new_string)

print('\n\n')
#### String Methods ####

# Calling the dir(directory) function shows all the methods you can do with a string.
# You can pass almost anything into the dir() function!
# In this basic guide, I've covered a small selection of useful methods

print(dir(str))


# A method is an action that can be performed on a variable
# Each type (str, int, bool etc..) has its own set of methods
# String methods don't 'change' the original variable, instead they return new data!

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
# Only capitalizes the first letter of the entire string not each individual word!
drink_capitalized = drink.capitalize()
print(drink_capitalized)


# Splitting the string apart into a list using split
# by default, this splits by any spaces in the string, but a character can also be specified, this is called the 'delimiter'
split_drink = drink.split()
print(split_drink)


# Splitting the string by the dash
fullname = 'Harry-James-Potter'
split_name = fullname.split('-')
print(split_name)


# Replacing characters in the string with alternatives
# This example replaces the small e with a big one!
lowered_vowels = 'CHeSTeR'
uppered_vowels = lowered_vowels.replace('e', 'E')
print(uppered_vowels)


# Strip is used to remove leading and trailing whitespaces
url = '  google  '
website = 'www.' + url.strip() + '.com'
print(website)


print('\n\n')

#### String Methods 2 ####
# I've added the next couple of methods as a different section,
# simply because they return True or False, rather than returning a new string

# These methods evaluate the string in a special way, and
# if the condition is true, then the boolean 'True' is returned.


# the string.islower() returns True if the string in question
# contains only lower case characters. in this case, the variable
# 'valid' contains a value of True

username = 'jamescuk'
valid = username.islower()
print(valid)

# lets do this again with a slice of the string
# This is asking if the first 4 characters in the string are lower case
first_4_chars_valid = username[:4].islower()
print(first_4_chars_valid)


# lets do it in a simple if/else statement!
if username.islower():
    print(username, 'Is valid and good to go!')
else:
    print(username, 'is not valid..')


# All of the operations above can also be repeated with the methods to follow, they just look for different things!

day_of_week = 'Wednesday'

# the str.istitle() method returns True only if the string is in title case

# (has a single capital letter only at index 0)
is_valid_day = day_of_week.istitle()
print(is_valid_day)


# the str.isupper() method returns True if word is entirely in upper case!
word = 'HEY'
is_angry = word.isupper()
print(is_angry)

## The str.isdigit() method returns True if every element is a number
serial_number = '123456' # This is True
serial_number_v2 = 'onetwo3456' # This is False
print(serial_number.isdigit())
print(serial_number_v2.isdigit())


# The str.isalpha() method returns True if every character is a letter, (no spaces, punctuation or numbers!)

favourite_language = 'Python'
print(favourite_language.isalpha())


print('\n\n')
#### Some useful built in functions ####

# len()
# This is used to return the length of the string

string_a = 'cheese'
print(string_a, 'has', len(string_a), 'characters')

# sorted()
# This returns a list, but will sort the characters alphabetically
print(sorted(string_a))


# int(), float()
# Converts the string to an int or float respectively
# The string must be in the correct format, or a ValueError will occur

# b is the integer version of a!
a = '55'
b = int(a)
print(b)

# c is the float version of a
c = float(a)
print(c)
