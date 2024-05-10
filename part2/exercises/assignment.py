#! part2/exercises/script.py

# Initializing a variable 'answer' with the integer value 42.
answer = 42

# Assigning 'insight' to reference the same integer object as 'answer'.
# In Python, integers are immutable and Python optimizes resource usage by reusing objects for small integers.
insight = answer  

# Checking if 'answer' and 'insight' have the same value. The '==' operator checks for value equality.
# This condition will be True as both variables hold the value 42.
if answer == insight:
    print("answer '==' insight: True (They have the same value)")

# Checking if 'answer' and 'insight' refer to the same object in memory. The 'is' operator checks for identity equality.
# This condition will be True as 'insight' is assigned to 'answer', hence both point to the same integer object 42.
if answer is insight:
    print("answer 'is' insight: True (They refer to the same object)")

# Printing the memory IDs of 'answer' and 'insight'.
# The id() function returns the memory location of the object each variable refers to.
# As both variables refer to the same object, they will have the same memory ID.
print(f"Answer has a memory id of - {id(answer)} and Insight has a memory of {id(insight)}")
