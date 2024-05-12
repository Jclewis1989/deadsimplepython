# Demonstrating different methods to create shallow copies in Python

# Shallow copy of a list
original_list = [1, 2, 3, [4, 5]]

# Method 1: Using slicing
copied_list_slicing = original_list[:]

# Method 2: Using the list() constructor
copied_list_constructor = list(original_list)

# Method 3: Using list comprehension
copied_list_comprehension = [x for x in original_list]

print("Original List:", original_list)
print("Copied List (slicing):", copied_list_slicing)
print("Copied List (constructor):", copied_list_constructor)
print("Copied List (comprehension):", copied_list_comprehension)

# Shallow copy of a dictionary
original_dict = {'a': 1, 'b': [2, 3]}

# Method 4: Using the dict() constructor
copied_dict_constructor = dict(original_dict)

# Method 5: Using the copy() method
copied_dict_copy_method = original_dict.copy()

# Method 6: Using dictionary comprehension
copied_dict_comprehension = {k: v for k, v in original_dict.items()}

print("\nOriginal Dictionary:", original_dict)
print("Copied Dictionary (constructor):", copied_dict_constructor)
print("Copied Dictionary (copy method):", copied_dict_copy_method)
print("Copied Dictionary (comprehension):", copied_dict_comprehension)

# Shallow copy of a set
original_set = {1, 2, 3}

# Method 7: Using the copy() method
copied_set = original_set.copy()

print("\nOriginal Set:", original_set)
print("Copied Set (copy method):", copied_set)

# Modifying the mutable elements to show that the copies are shallow
original_list[3].append(6)
original_dict['b'].append(4)

print("\nAfter modification:")
print("Original List:", original_list)
print("Copied List (slicing):", copied_list_slicing)
print("Original Dictionary:", original_dict)
print("Copied Dictionary (copy method):", copied_dict_copy_method)

