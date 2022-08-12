# Python numbers
var1 = 1        # Interger
var2 = 10.0     # Float
var3, var4 = 3.14j, 2+5j    # Complex

print(var1)
print(var2)

print(var3, end='\t')
print(type(var3))
print(var4, end='\t')
print(type(var4))

print(var3+var4)


# Deleteting objects
# del var1
del var1, var2
# print(var1) cannot work as var1 is already deleted