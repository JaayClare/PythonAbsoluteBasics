### I have left all the print statements uncommented!
### You may wish to go through and comment out parts that you aren't currently looking at
### This guide is by no means super detailed! It's aimed purely at beginners to show the absolute basics.




numbers = [10,20,30,40,50]


### Adding Elements ###
# append: Adds one element to the end of the list
# insert: Adds one element at a given index
# extend: Adds multiple items one-by-one to the end. This method takes an iterable such as a list or string

print('List, before additions:', numbers, '\n')

numbers.append(60) # Adds 60 to the end of the list
numbers.insert(0, 'Zero') # Adds 'Zero' to position 0 in the list
numbers.extend([60, 70,80,90]) # Individually adds 60,70,80 & 90 to the end of the list

print('List, after additions:', numbers, '\n')



### Returning Information about the list ###
# count: Shows how many times a given element appears
# index: Shows the first index of a given element in the list
elem = 60
count_of_element = numbers.count(elem)
print('elem {} appears {} times\n'.format(elem, count_of_element))

position_of_element = numbers.index(elem)
print('Number {} appears first at position {}\n'.format(elem, position_of_element))


### Removing Elements from the list ###
# pop: Removes and returns the last variable (An index can be passed in to specify the element)
# remove: Removes a given element from the list
# clear: Clears the entire list and leaves it blank

# Note: clear removes all element and keeps the empty list,
# the del() function deletes the entire reference to the list

removed_elem = numbers.pop() # Removes the last element from numbers and gives it to the removed_elem variable
first_elem = numbers.pop(0) # Removes first element from numbers and gives it to the first_elem variable

print('Removed Element(last): ', removed_elem)
print('Removed Element(first): ', first_elem)
print('Numbers after the pop methods:', numbers)

numbers.remove(40) # Removes the element '40' from the list

print('Numbers after the remove method has been ran:', numbers)


numbers.clear()


print('Numbers after the clear method has been ran:', numbers)




### Rearranging the list ###
# reverse: Reverses a list in-place
# sort: Sorts a list in ascending order, in-place

# Note: 'in-place' means to modify the original without making a new copy

letters = ['A', 'C', 'D', 'M', 'B', 'L']
print('Letters before any changes:', letters)

letters.reverse() # Reverses the order of the list permanently

print('Letters after reversal:', letters)

letters.sort() # Sorting into ascending order

print('letters after sorting', letters)

letters.sort(reverse=True) # Sorting into ascending order

print('letters after sorting backwards', letters)



### Copying the list
# copy: Returns a copy of the list which is totally unlinked from the original

floats = [1.0, 2.0, 3.0, 4.0, 5.0]

floats_copy = floats.copy() # Copying the floats list to a new variable
# Whatever is done to 'floats_copy' will be independent of the original list
# because they are unlinked!

print('\n\n')
