### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.

### Enjoy :)


### Integers and Floats are the two main types of numbers that you'll be using in Python


#### Integers ####

# Integers are any positive/negative whole number, including 0
a = 100
b = -150
c = 0


# As seen in video 2, integers can be manipulated using a range of operators
# Check out the 'Operators.py' file for a run through of all the operations


# The type function shows that the variable a is an int.
# This function is useful to use when checking the type of a variable before doing an operation
print(type(a))

# Integers are 'unbounded', this means that there is no limit on their size, it all depends on how much memory your PC has!
# This means that Python is able to handle really large numbers!

# Integers can also be created using the int() function.
# To successfully convert another variable into an int, consider the following two examples.

# If converting a string, the integer must have no lettering inside.
int_as_str = '100'
y = int(int_as_str)


# If converting a float, just be aware that the number will be rounded down!
some_float = 6.66
z = int(some_float)
print(z)

# It's also possible to access a subset of a string using slicing, and convert this!
name_age = 'John 30'
persons_age = int(name_age[5:])
print(persons_age)


# We can also convert a list element into a string!
# This is saying: Go to index 0, the element there is now equal to the integer version of the same element!
ages = ['10', '20', '30']
ages[0] = int(ages[0])

print('\n\n')
#### Floats ####

# Floats are any positive or negative decimal number, including 0.0

# Floats are not entirely 100% accurate for reasons I wont' explain here!
# It's essentially down to how computer hardware stores floating point numbers as binary fractions.
# For small floats, it's fine! However.. You may notice rounding issues with particulary large numbers.


# Floats are returned by default when doing regular division
# Even though 100 / 20 divides evenly, we still get a float back
number_1 = 100
number_2 = 20
result = number_1 / number_2
print(result)


# Any mathematical operation involving a float, means the answer will be a float
# The result of the answer below is a float because of the 1.0 at the end.
print(10 * 10 + 1 ** 2 + 1.0)


#### Limitations ####

# When Indexing/Slicing, only integers can be used!
name = 'Brenda'

# This works!
print(name[0])

# This does not!
# print(name[0.0])

# This works!
f = 0.0
print(name[int(f)])


# In the range function, only integers can be used

# This one works!
list_of_nums = list(range(1, 20))

# This one does not!
# list_of_nums = list(range(1.0, 20.0))

print(list_of_nums)

print('\n\n')
#### Useful Built-In functions for Floats/Ints ####


# the pow() function raises one number to the power of another
# The first number is the 'Base', the second is the 'Exponent'
# So.. 10 to the power of 5.. (10 is the base, 5 is the exponent) = 10 x 10 x 10 x 10 x 10

print(pow(10, 5))


# The round function rounds a float down to either an int, or a set  number of points after the decimal
a_float = 5.11111

# To no decimal places..
print(round(a_float))

# To 2 decimal places..
print(round(a_float, 2))


# The abs function returns the absolute value of a number
# the absolute value is simply its distance away from 0, so 10 and -10 both have the same absolute value

value1 = 100
value2 = -100
# Both abs() functions return the same!
print(abs(value1), abs(value2))
