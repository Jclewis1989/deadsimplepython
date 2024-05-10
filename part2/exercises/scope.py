# Example of Python Scopes: Local, Enclosing, Global, Built-in

# Global scope
x = 'global x'

def test():
    # Enclosing scope
    y = 'enclosing y'
    
    def inner():
        # Local scope
        x = 'local x'  # This 'x' is local to the inner() function
        print(x)  # Prints 'local x', accessing the local scope variable
        print(y)  # Prints 'enclosing y', accessing the variable in the enclosing scope
    
    inner()
    print(x)  # Prints 'global x', accessing the global variable since there's no local 'x' in test()

# Built-in scope
print(str(10))  # 'str' is a built-in Python function which is accessible globally

test()
print(x)  # Prints 'global x', demonstrating access to the global variable

# Example Output:
# local x
# enclosing y
# global x
# 10
# global x
