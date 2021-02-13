# Operators sit in the middle and are the 'action'
# The operands are either side of the operator


#### Mathematical Operators ####
print('Mathematical Operators\n\n')
x = 10
y = 5

a = x + y
# a has the sum of x and y (10 + 5)


b = x - y
# b has the value of x minus y (10 - 5)

c = x * y
# c has the value of x times y (10 X 5)

d = x / y
# d has the value of x divided by y (10 / 5)
# d becomes a float (decimal number) even if
# the number divides evenly

e = x // y
# d has the value of x floor divided by y (10 // 5)
# this always returns a whole number (integer)
# which is rounded down

f = x ** y
# f has the value of 10 to the power of y
# (10 x 10 x 10 x 10 x 10)

g = x % y
# g has the value of x mod y
# Modulus returns the remainder of whole division
# How to calculate modulus:

# Example. 20 mod 6

# 1. Divide 20 by 6 (6,12,18 - fits in 3 times)
# 2. Record the remainder (the remainder is 2)
# 3. the remaider is your answer, so 20 mod 6 is 2!

# 100 mod 30
# 30,60,90.. remainder 10, so the answer is 10!

print('{} + {} = {}\n'.format(x, y, a))
print('{} - {} = {}\n'.format(x, y, b))
print('{} * {} = {}\n'.format(x, y, c))
print('{} / {} = {}\n'.format(x, y, d))
print('{} // {} = {}\n'.format(x, y, e))
print('{} ** {} = {}\n'.format(x, y, f))
print('{} % {} = {}\n'.format(x, y, g))


#### Conditional Operators ####
print('Conditional Operators\n\n')

# These are used to evaluate a situation as either True(yes) or False(no)

# == is equal to
# != is not equal to
# > is more than
# < is less than
# >= is more than or equal to
# <= is less than or equal to

value_1 = 100
value_2 = 200

# The evalaution of all the statements below are done inside
# the print function so the result of the evaluation is then
# shown to the screen, either True or False


print(value_1 == value_2, '\n')
# prints False: 100 is not equal to 200!

print(value_1 != value_2, '\n')
# prints True: 100 is not equal to 200!


print(value_1 > value_2, '\n')
# prints False: 100 is not more than 200


print(value_1 < value_2, '\n')
# prints True: 100 is less than 200


print(value_1 >= value_2, '\n')
# prints False: 100 is not more or equal to200


print(value_1 <= value_2, '\n')
# prints True: 100 is less than or equal to 200



#### Assignment Operators ####
print('Assignment Operators\n\n')

# These are used to assign values to variables

# = equal to
# += equal to itself plus another value
# -=  equal to itself minus another value
# *=  equal to itself multiplied by another value
# /=  equal to itself divided by another value
# //=  equal to itself floor divided by another value
# **=  equal to itself to the power of another value
# %=  equal to itself modded by another value

value_1 = 10
print('Value 1 before.. {}'.format(value_1))
value_1 += 5
# Value 1 is now (10 + 5)
print('Value 1 after.. {}\n'.format(value_1))


value_2 = 50
print('Value 2 before.. {}'.format(value_2))
value_2 -= 25
# Value 2 is now (50 - 25)
print('Value 2 after.. {}\n'.format(value_2))


value_3 = 100
print('Value 3 before.. {}'.format(value_3))
value_3 *= 1.5
# Value 3 is now (100 X 1.5)
print('Value 3 after.. {}\n'.format(value_3))


value_4 = 1000
print('Value 4 before.. {}'.format(value_4))
value_4 /= 200
# Value 4 is now (1000 / 200)
print('Value 4 after.. {}\n'.format(value_4))


value_5 = 1000
print('Value 5 before.. {}'.format(value_5))
value_5 //= 200
# Value 5 is now (1000 // 200) - floor divided!
# Same as previous example, but as an int instead of a float
print('Value 5 after.. {}\n'.format(value_5))


value_6 = 5
print('Value 6 before.. {}'.format(value_6))
value_6 **= 3
# Value 6 is now 5 to the power of 3
print('Value 6 after.. {}\n'.format(value_6))


value_7 = 25
print('Value 7 before.. {}'.format(value_7))
value_7 %= 4
# Value 7 is now 25 mod 4 (25 mod 4 = 1)
print('Value 7 after.. {}\n'.format(value_7))
