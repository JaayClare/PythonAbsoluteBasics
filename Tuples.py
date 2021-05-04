
### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.



# Tuples can be seen as immutable lists!
# Indexing, printing, slicing is done all the same
# The only visual difference is the rounded parentheses, rather than the square brackets


numbers = (10,20,30,40,50,10,10)


# This will not work because the tuple is immutable!
# numbers[0] = 100


# Both of these lines work just like they do with a list
# print(numbers[0])
# print(numbers[:3])



### The tuple has only 2 methods available to use

# count: returns how many times a given element appears in the tuple
print(numbers.count(10))


# index: Returns the first occurence of a given element in the list
print(numbers.index(20))
