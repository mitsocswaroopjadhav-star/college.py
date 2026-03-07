# Program to perform basic operations on Sets

# 2.1) Create and access set elements
print("2.1) Create and access set elements")
my_set = {10, 20, 30, 40, 50}
print("Original Set:", my_set)

# Accessing elements
# Note: Sets are unordered and do not support indexing (e.g., my_set[0] is invalid).
# We access elements by iterating or checking membership.
print("Iterating through set elements:")
for item in my_set:
    print(item, end=" ")
print("\n")

# Checking for membership
print("Is 20 in the set?", 20 in my_set)
print()

# Define two sets for set operations
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print()

# 2.2) Union of the elements
print("2.2) Union of the elements")
# Union returns all distinct elements from both sets
union_set = set_A.union(set_B)
print("Union (A | B):", union_set)
print()

# 2.3) Intersection of the elements
print("2.3) Intersection of the elements")
# Intersection returns elements common to both sets
intersection_set = set_A.intersection(set_B)
print("Intersection (A & B):", intersection_set)
print()

# 2.4) Difference of the elements
print("2.4) Difference of the elements")
# Difference (A - B) returns elements in A that are not in B
diff_set = set_A.difference(set_B)
print("Difference (A - B):", diff_set)
print("Difference (B - A):", set_B.difference(set_A))