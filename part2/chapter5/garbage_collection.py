import sys

# Create an object with a value 3000 (which is not an immediately reusable integer in Python)
a = 3000

# Check the reference count
print("Reference count for 3000:", sys.getrefcount(a) - 1)  # subtract 1 to exclude the getrefcount call itself

# Assign another name to the same object
b = a

# Now the reference count increases
print("Reference count for 3000 after adding b:", sys.getrefcount(a) - 1)

# Delete one reference
del a

# a is no longer accessible, but the object 3000 still exists, referenced by b
print("Reference count for 3000 after deleting a:", sys.getrefcount(b) - 1)  # now using b to check count

# b is still a valid reference to the object
print("Value of b:", b)

# Deleting b will reduce the reference count to zero, assuming no other references exist
del b

# Now the object 3000 is eligible for garbage collection, as there are no references to it
