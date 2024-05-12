#! part2/exercises/script.py

# Initialize a variable 'answer' with the integer 42
answer = 42

# Assign 'insight' to reference the same object as 'answer'.
# Python optimizes small integers by using the same object for all references to the same integer value.
insight = answer  

# Check if 'answer' and 'insight' have the same value. They should, as both are 42.
if answer == insight:
    print("answer '==' insight: True (They have the same value)")

# Check if 'answer' and 'insight' refer to the same object in memory.
# This will be True because 'insight' is directly assigned from 'answer'.
if answer is insight:
    print("answer 'is' insight: True (They refer to the same object)")

# Display the memory IDs of 'answer' and 'insight'.
# The id() function returns the memory location of the object.
# Since both variables point to the same integer object, their memory IDs will be the same.
print(f"Memory ID of 'answer': {id(answer)}; Memory ID of 'insight': {id(insight)}")

def modify_list(items):
    # Check if list is not empty
    if items:
        # Modify the first element of the list
        items[0] = "Modified"
    # Append a new element to the end of the list
    items.append("New item")
    print("Inside function:", items)

# Define the original list
original_list = ["Original item", "Another item"]

# Modify the list through the function
modify_list(original_list)

# Print the list after function call to observe the modification effects
print("Outside function:", original_list)
