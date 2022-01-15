### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.


# Control flow is used to guide the flow of execution during the running of a program
# The most simple form of control flow is an if statement

x = 10
y = 5
if x > y:
    print(x, 'Is larger than 5')

# The above example performs a check, we call a 'condition'
# The condition is evaluated to see if it is True, or False
# If the condition is True, then the code indented underneath is executed

# A condition can also be evaluated inside a print statement
#print(x > y) # This shows True!

password = 'yes123'
saved_password = 'Yes1234'

if password == saved_password:
    print('Looks good!')
else:
    print('Passwords do not match')



# The Boolean Operators 'and' or 'or' can also be used to check more complex conditions

name = 'James'
age = 30

if name == 'James' or name == 'Alex' and age > 25:
    print('Hi', name)



# To expand the if statement, an 'else' can also be added which is only triggered
# if the if statement's condition is false.
# This can be thought of as 2 individiual pathways
# If a condition is True, do something.. if not, do something else!

language = 'Python'

if language == 'python':
    print('Good Choice!')  # Runs if the 'if' condition is True
else:
    print('Oh dear..') # Runs if the 'if' condition is True


# To really make control flow more interesting and offer more pathways
# the concept of 'if, elif, else' can be introduced.
# This allows for more conditions to be looked at, rather than 1!

# The if statement is ran first, and if True, the whole block ends
# If false, then fhe first elif is ran and the same check is made
# If any of the elifs are True then this is also when the block ends


exam_score = 75

if exam_score >= 90:
    print('A Grade')
elif exam_score >= 80 and exam_score < 90:
    print('B Grade')
elif exam_score >= 70 and exam_score < 80:
    print('C Grade')
elif exam_score >= 60 and exam_score < 70:
    print('D Grade')
else:
    print('Fail')

# In the above example, the if statement is run first.
# then the 3 elifs, then finally the else!
# If at any point, the condition for one of the statements is True, the whole process ends
# then the print statement underneath is ran.
