#!python3

a = True
b = False
print("NOT a:", "not a results in", not a)
print("NOT b:", "not b results in", not b)

# In theory
print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)
print()

# In practice
print("(5 > 2) and (3 > 2) =", (5 > 2) and (3 > 2))
print("(5 > 2) and (3 < 2) =", (5 > 2) and (3 < 2))
print("(5 < 2) and (3 > 2) =", (5 < 2) and (3 > 2))
print("(5 < 2) and (3 < 2) =", (5 < 2) and (3 < 2))

# In theory
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)
print()

# In practice
print("(5 > 2) or (3 > 2) =", (5 > 2) or (3 > 2))
print("(5 > 2) or (3 < 2) =", (5 > 2) or (3 < 2))
print("(5 < 2) or (3 > 2) =", (5 < 2) or (3 > 2))
print("(5 < 2) or (3 < 2) =", (5 < 2) or (3 < 2))

