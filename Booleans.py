### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.

### Enjoy :)

# A Boolean (or bool) can have two possible values, True or False

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

# Print is obviously useful for showing outputs on the screen, but it can also evaluate a statement and show True/False
