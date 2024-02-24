#tuple -  Tuples in Python are similar to lists, but they are immutable, meaning once a tuple is created, its contents cannot be changed. 
# Creating a Tuple: A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
my_tuple = (1, 2, 3)
single_element_tuple = (1,)  # Note the comma for a single-element tuple
empty_tuple = ()

#Accessing Tuple Elements: Similar to lists, elements can be accessed via indexing and slicing.
element = my_tuple[0]  # Access the first element
sub_tuple = my_tuple[1:3]  # Slice the tuple

#Concatenation: Combining tuples to form a new tuple.
concatenated_tuple = (1, 2, 3) + (4, 5, 6)

#Repeating Tuples: Repeating the elements of a tuple a specified number of times.
repeated_tuple = (1, 2, 3) * 2

'''
Immutable Nature: Tuples cannot be changed after they are created. Attempting to modify an element of a tuple results in a TypeError.
Nested Tuples: A tuple can contain other tuples as elements.
'''
nested_tuple = (1, (2, 3), 4)

# Intermediate Operations
# Unpacking: Assigning elements of a tuple to multiple variables.
# Creating a tuple for demonstration
# Unpacking the tuple
a, b, c = my_tuple
print("Unpacked values:", a, b, c)
# Output: Unpacked values: 1 2 3

# Tuple Membership Test
exists = 2 in my_tuple
print("Does 2 exist in the tuple?", exists)
# Output: Does 2 exist in the tuple? True

# Iterating Through a Tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3

# Tuple Length
length = len(my_tuple)
print("Length of the tuple:", length)
# Output: Length of the tuple: 3

# Tuple Index
index = my_tuple.index(2)
print("Index of 2 in the tuple:", index)
# Output: Index of 2 in the tuple: 1

# Counting Elements
count = my_tuple.count(1)
print("Count of 1 in the tuple:", count)
# Output: Count of 1 in the tuple: 1

# Advanced tuple operation
# Tuple to list
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)
temp_list.append(4)  # Modifying the list
my_tuple = tuple(temp_list)  # Converting back to tuple
print("Tuple after conversion and modification:", my_tuple)
# Output: Tuple after conversion and modification: (1, 2, 3, 4)

# Using Tuples as Keys in Dictionaries - Tuples, being immutable, can be used as keys in dictionaries, allowing for complex key structures.
# Tuples as dictionary keys
coordinates = {(1, 2): "Point A", (3, 4): "Point B"}
print("Dictionary with tuple keys:", coordinates)
# Output: Dictionary with tuple keys: {(1, 2): 'Point A', (3, 4): 'Point B'}


# Comparing tuples- Tuples can be compared using comparison operators. 
#This comparison is done lexicographically.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Is tuple1 less than tuple2?", tuple1 < tuple2)
# Output: Is tuple1 less than tuple2? True

'''
Named Tuples
Named tuples provide a way to assign names to the elements in a tuple, making the code more readable and self-documenting.
'''
from collections import namedtuple

# Creating a named tuple - Part of the collections module, named tuples allow for tuple elements to be accessed by name, improving code readability.
Point = namedtuple('Point', ['x', 'y'])
pt1 = Point(1, 2)  # Creating a Point object
print("Named tuple Point:", pt1)
print("Accessing x coordinate:", pt1.x)
# Output:
# Named tuple Point: Point(x=1, y=2)
# Accessing x coordinate: 1







