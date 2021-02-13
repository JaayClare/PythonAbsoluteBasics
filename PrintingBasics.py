# print is a function which shows an output to the shell
# print is a builtin function, so it doesn't need to be imported
# and it can be access from anywhere in the program


# prints 'Hello World' to the shell
print('Hello World')

# printing text(strings) can be done in either single
# or double quotes, just don't mix!

print('This is ok')
print("This is ok too!")


# The items we put inside the print function
# are called arguments, and many can be added
# as long as they as are separated by commas

print('Just..', 'Like..', 'This')

# By default, a space is added, but this can be changed
# by overwriting the 'sep' argument, which is short
# for separator

print('Yes', 'No', 'Maybe', sep='-')

# New lines can also be added using the special
# newline character which is a backslash and an 'n'

print('My\nname\nis\nJames')


# Variables can be printed by passing in the identifier,
# in this example there is a mix of strings and variables

name = 'James'
location = 'England'
print('I am', name, 'From', location)
