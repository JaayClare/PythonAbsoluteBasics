### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.


# A set is created using curly braces
numbers = {10,32,12,6,5,4}

# An empty set is created by calling the set function
empty_set = set()
print(empty_set)


# In this set, the duplicate 1's are removed
a = {1,1,1,1,1,2,3,4}
print(a)

# Ordering does not matter with sets
print({1,2,3} == {3,2,1}) # True

# Whereas, with a list it does!
print([1,2,3] == [3,2,1]) # False



##### Set Operations #####
# All 4 operations are shown with the regular method being applied
# They are also shown with their operator which does the same job

a = {1,2,3,4}
b = {3,4,5,6}


## Union ##
## (Both sets merged)
set_union = a.union(b)

print(set_union)
print(a | b, '\n')

## Intersection ##
## (Only elements that exist in both sets)

set_inter = a.intersection(b)
print(set_inter)
print(a & b, '\n')


## Symmetric Difference ##
## Only elements that exist in one set, but not both

set_sd = a.symmetric_difference(b)
print(set_sd)
print(a ^ b, '\n')


## Difference ##
# Taking away one set from the other

set_diff = a.difference(b)
print(a - b, '\n')


##############################
# Subsets and Supersets


names = {'John', 'Jo', 'Ian', 'Sarah', 'Alex'}
group = {'Jo', 'Ian'}

# 'group' is a subset of 'names'
# therefore, 'names' is the superset of 'group'

print(group.issubset(names)) # True
print(names.issuperset(group)) # True


##############################
# letters starts off as a list with duplicates
letters = list('aabbccdd')
print('pre:', letters)

# Converting from list -> set -> list
letters = list(set(letters))

print('post:', letters)
