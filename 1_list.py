# Program to perform basic operations on Lists

# 1.1) Create and access list elements
print("1.1) Create and access list elements")
numbers = [10, 20, 30, 40, 50]     # Creating a list
print("Original list:", numbers)

# Accessing elements
print("First element (numbers[0]):", numbers[0])
print("Third element (numbers[2]):", numbers[2])
print("Last element (numbers[-1]):", numbers[-1])
print("Slice from index 1 to 3 (numbers[1:4]):", numbers[1:4])
print()

# 1.2) Add and Remove list elements
print("1.2) Add and Remove list elements")

# Adding elements
numbers.append(60)                 # Add at the end
print("After append(60):", numbers)

numbers.insert(2, 25)              # Insert at index 2
print("After insert(2, 25):", numbers)

# Removing elements
removed = numbers.pop()            # Remove last element
print("After pop():", numbers, " | Removed element:", removed)

numbers.remove(25)                 # Remove first occurrence of value 25
print("After remove(25):", numbers)
print()

# 1.3) Sort list elements
print("1.3) Sort list elements")

# Sort in ascending order
numbers.sort()
print("Sorted in ascending order:", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)
print()

# 1.4) Reverse list elements
print("1.4) Reverse list elements")

# Method 1: Using reverse()
numbers.reverse()
print("After reverse() method:", numbers)

# Method 2: Using slicing
reversed_numbers = numbers[::-1]
print("Using slicing (numbers[::-1]):", reversed_numbers)