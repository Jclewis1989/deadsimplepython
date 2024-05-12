import copy

# Demonstrating deep copies in Python

# Deep copy of a list
original_list = [1, 2, 3, [4, 5]]

# Creating a deep copy of the list
deep_copied_list = copy.deepcopy(original_list)

print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

# Deep copy of a dictionary
original_dict = {'a': 1, 'b': [2, 3]}

# Creating a deep copy of the dictionary
deep_copied_dict = copy.deepcopy(original_dict)

print("\nOriginal Dictionary:", original_dict)
print("Deep Copied Dictionary:", deep_copied_dict)

# Deep copy of a set
original_set = {1, 2, 3, (4, 5)}

# Creating a deep copy of the set
deep_copied_set = copy.deepcopy(original_set)

print("\nOriginal Set:", original_set)
print("Deep Copied Set:", deep_copied_set)

# Modifying the mutable elements to show that the copies are independent
original_list[3].append(6)
original_dict['b'].append(4)

print("\nAfter modification:")
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)
print("Original Dictionary:", original_dict)
print("Deep Copied Dictionary:", deep_copied_dict)

# This script demonstrates that deep copies are completely independent from the original.
# Changes to the original data structures do not affect their deep copies.
