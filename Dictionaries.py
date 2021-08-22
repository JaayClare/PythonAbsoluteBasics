### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.



# a blank dictionary can be created with the empty curly braces

a_blank_dict = {}
print(type(a_blank_dict)) # Checked with the type() function




# The following dictionary consists of 3 entries
# Each entry consists of a key, and a value. Known as a 'key-value' pair
names_ages = {'Chris' : 55, 'Alex' : 41, 'Mark' : 27}

#################################################
# Accessing, setting and editing Items:


## Retrieving the value for Chris (55)
print(names_ages['Chris'])


# Setting a new key, with the value of 99
names_ages['John'] = 99


# Editing Alex's value to now be 42
names_ages['Alex'] = 42




#################################################
#  Keys, Values, Items
# These are all dynamic, so they will reflect any changes that have been made

# Extracting the keys:
print(names_ages.keys())

# Making a neat list out of the current keys in the dictionary
names = list(names_ages.keys())



# Extracting the values:
print(names_ages.values())

# Making a neat list out of the current values in the dictionary
ages = list(names_ages.values())


# Extracting the items:
# This returns essentially a list of tuples
# [(key, value), (key, value) etc...]
print(names_ages.items())

# Making a neat list out of the current items in the dictionary
na = list(names_ages.items())


########################
# Membership Check (seeing if a key is in the dictionary)

# Returns True because the key of John exists in the dictionary
print('John' in names_ages)


# Using the same logic to check for the presence of a key, before accessing it
name = 'Alex'
if name in names_ages:
    print(names_ages[name])


############################
