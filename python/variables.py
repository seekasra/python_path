# 
# Example file for variables
#

# Declare a variable and initialize it

f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
f = "abc" + str(1)
print(f)

# Global vs. local variables in functions
f = 0
def someFunction():
    global f #To ensure that you use the global f not local
    f  = "def"
    print(f)

someFunction()
print(f)

#You can undefine variables in Python! :)
del f
print(f)
