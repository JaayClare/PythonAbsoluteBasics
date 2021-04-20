### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.


# Try and Except aims to catch errors and run a different block of code instead


# We can often say we are 'catching an error', this means we are stopping it from crashing the
# rest of our program, and we are instead trying something else

# Consider this example:

#try
    # run this code!
#except:
    # do this instead (only if an error is raised in the above block)

# Python will try and run the code underneath try, but if an error is detected then
# it jumps to the code underneath except and runs that instead.
# The above example is a blanket exception that will catch any error.

# Whilst this works, it's normally best to catch specific errors




# Example 1:
# Catching a Name Error
# A NameError is raised when a variable that does not exist has been referenced.
# Maybe you spelt the variable name wrong, or tried to use it above where you defined it?

name  = 'James'
try:
    print(namee) # This line tries to run, but the variable has been spelt wrong
except NameError as e:
    print('NameError Detected')




# Example 2:
# Catching an Index Error
# An IndexError is raised when trying to access an index that does not exist
# So if a string contains 5 characters, and you try to access charcter 10.. its not possible!
# This is when an IndexError is raised


food = 'Salmon'

try:
    idx = 10
    print(food[idx]) # idx is too big for the size of the string, the max index is 5
except IndexError:
    print('Index was too for down!')




# Example 3:
# Catching a ValueError
# A ValueError can often happen when trying to convert between types and the conversion is inappropriate
# For example, the following code is perfectly fine

str_float = '10.0'
# The conversion to float is ok because the string is properly formed
new_float = float(str_float)


# the example below is an incorrect conversion, so a ValueError will be raised
# bad_str_float = 'ten point five'
# new_bad_float = float(bad_str_float)


# lets catch it!
try:
    bad_str_float = 'ten point five'
    new_bad_float = float(bad_str_float)
except ValueError:
    print('Conversion failed')
