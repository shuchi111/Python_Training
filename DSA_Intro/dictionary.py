'''Dictionary- Dictionaries in Python are versatile data structures that store key-value pairs.
Keys must be unique and immutable (e.g., strings, numbers, or tuples that contain only immutable elements), 
making dictionaries ideal for fast data lookup
'''
# Basic operation

# Empty dictionary
empty_dict = {}

# Dictionary with integer keys
int_keys_dict = {1: 'apple', 2: 'banana'}

# Dictionary with mixed key types
mixed_keys_dict = {'name': 'John', 1: [2, 4, 3]}


#Accessing Elements
# Accessing value by key
print(int_keys_dict[1])
# Output: apple

# Using get() to access values
print(mixed_keys_dict.get('name'))
# Output: John

#Adding and Updating Elements
# Adding a new key-value pair
int_keys_dict[3] = 'orange'

# Updating an existing key
int_keys_dict[2] = 'banana updated'

# Removing a particular item
del int_keys_dict[2]

# Removing the last inserted item
int_keys_dict.popitem()

# Removing an item by key
int_keys_dict.pop(1)

#Intermediate Operations
# Iterating over keys
for key in int_keys_dict:
    print(key)

# Iterating over values
for value in int_keys_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in int_keys_dict.items():
    print(key, value)

# Dictionary Comprehensions
# Creating a new dictionary with squared valuesMerging Dictionaries
squared_dict = {x: x**2 for x in range(6)}
print(squared_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}

# Advanced topics
'''
Dictionary Views: Keys, Values, and Items
Dictionary methods .keys(), .values(), and .items() return view objects that provide a dynamic view of the dictionary entries, which means they change when the dictionary changes.

Using defaultdict
The collections.defaultdict type automatically initializes dictionary entries to default values when new keys are accessed.

'''
from collections import defaultdict

dd = defaultdict(int)
dd['key1'] += 1
print(dd['key1'])
# Output: 1

'''
Ordered Dictionaries (OrderedDict)
Before Python 3.7, dictionaries did not maintain insertion order.
OrderedDict from the collections module was used to preserve order. 
Now, all Python dictionaries maintain insertion order by default, but OrderedDict can still be useful for its additional functionality, such as reversing the order.
'''
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2)])
od['c'] = 3
print(list(od.keys()))
# Output: ['a', 'b', 'c']

#Dictionary Membership Test
#Checking for the existence of a key in a dictionary
print('a' in od)
# Output: True






