#list


# Creating a list
my_list = [1, 2, 3, 4, 5]  # A simple list of integers
empty_list = []  # An empty list
mixed_list = [1, "Hello", 3.14, True]  # A list with mixed data types

# Accessing list elements
first_element = my_list[0]  # Accessing the first element
last_element = my_list[-1]  # Accessing the last element

# Slicing lists
sub_list = my_list[1:3]  # Gets a sublist from index 1 to 2, excluding index 3
reverse_list = my_list[::-1]  # Reverses the list

# Modifying a list
my_list[0] = 10  # Changes the first element to 10
my_list.append(6)  # Appends 6 to the end of the list
my_list.insert(1, 20)  # Inserts 20 at index 1
my_list.extend([7, 8, 9])  # Appends elements of another list to the end

# Removing elements
my_list.remove(10)  # Removes the first occurrence of 10
popped_element = my_list.pop()  # Removes and returns the last element
my_list.pop(1)  # Removes the element at index 1

# Checking if an item exists in a list
exists = 5 in my_list  # Returns True if 5 is in my_list, else False

# List length
length = len(my_list)  # Returns the number of items in my_list

# Sorting lists
my_list.sort()  # Sorts my_list in ascending order
my_list.sort(reverse=True)  # Sorts my_list in descending order

# Reversing a list
my_list.reverse()  # Reverses the elements of my_list in place

# Copying a list
list_copy = my_list.copy()  # Creates a shallow copy of my_list
list_copy_deep = my_list[:]  # Another way to create a shallow copy

# List Comprehension: A concise way to create a new list by applying an expression to each element in an existing list.
squared = [x**2 for x in my_list]  # Creates a new list with squares of my_list elements

# Looping through a list- Iterating over each element in the list, executing a block of code for each element.
for item in my_list:
    print(item)  # Prints each item in my_list

# Index of an item
index = my_list.index(3)  # Returns the index of the first item whose value is 3

# Counting occurrences of an element - Counting how many times an element appears in the list.
count = my_list.count(3)  # Returns the number of times 3 appears in my_list

# Converting list to a string
my_list_str = ', '.join(map(str, my_list))  # Converts the list into a string

# Clearing all items from a list
my_list.clear()  # Removes all items from my_list

# Nested lists (lists within a list)
nested_list = [[1, 2, 3], [4, 5, 6]]  # A list containing two lists

