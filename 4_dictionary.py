# Program to perform basic operations on Dictionaries

# 4.1) Create and access dictionary elements
print("4.1) Create and access dictionary elements")
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original Dictionary:", my_dict)

# Accessing elements
# Access by key
print("Name (using key):", my_dict['name'])
# Access using get() method (safer if key might not exist)
print("Age (using get):", my_dict.get('age'))
print()

# 4.2) Update Dictionary
print("4.2) Update Dictionary")
# Updating an existing value
my_dict['age'] = 26
print("Updated Age:", my_dict)

# Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print("Added Email:", my_dict)
print()

# 4.3) Removing Elements
print("4.3) Removing Elements")
# Using pop() removes the item with the specified key and returns its value
removed_val = my_dict.pop('city')
print("After pop('city'):", my_dict)
print("Removed value:", removed_val)

# Using del keyword to remove an item
del my_dict['age']
print("After del my_dict['age']:", my_dict)
print()

# 4.4) Merging dictionaries
print("4.4) Merging dictionaries")
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
print("Dictionary A:", dict_a)
print("Dictionary B:", dict_b)
# Using update() to merge dict_b into dict_a
dict_a.update(dict_b)
print("Merged Dictionary:", dict_a)