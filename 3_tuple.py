# Program to perform basic operations on Tuples

# 3.1) Create and access tuple elements
print("3.1) Create and access tuple elements")
# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# Accessing elements
# Tuples support indexing and slicing like lists
print("First element (my_tuple[0]):", my_tuple[0])
print("Last element (my_tuple[-1]):", my_tuple[-1])
print("Slice from index 1 to 4 (my_tuple[1:4]):", my_tuple[1:4])
print()

# 3.2) Nested Tuple
print("3.2) Nested Tuple")
# A tuple can contain other tuples or mutable objects like lists
nested_tuple = ("Python", (1, 2, 3), ["a", "b"])
print("Nested Tuple:", nested_tuple)

# Accessing elements inside the nested structures
print("Element from inner tuple (nested_tuple[1][1]):", nested_tuple[1][1])
print("Element from inner list (nested_tuple[2][0]):", nested_tuple[2][0])
print()

# 3.3) Repetition of tuple
print("3.3) Repetition of tuple")
tuple_rep = ('Hi', 'Bye')
print("Original Tuple:", tuple_rep)
# Using the * operator repeats the tuple
print("Repeated Tuple (tuple_rep * 3):", tuple_rep * 3)
print()

# 3.4) Concatenation of tuples
print("3.4) Concatenation of tuples")
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
print(f"Tuple A: {tuple_a}")
print(f"Tuple B: {tuple_b}")
# Using the + operator joins tuples
print("Concatenated Tuple (tuple_a + tuple_b):", tuple_a + tuple_b)