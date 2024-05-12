import copy

# Shallow copy example
original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[2].append(5)  # Modifying a nested list

print("Original after shallow copy modify:", original_list)  # Output will show the modified nested list

# Deep copy example
original_list_deep = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list_deep)
deep_copied_list[2].append(5)  # Modifying a nested list

print("Original after deep copy modify:", original_list_deep)  # Output will not show the modified nested list
