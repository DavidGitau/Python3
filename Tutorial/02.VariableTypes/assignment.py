# Assigning Values to Variables
counter = 100       #An Integer value
miles = 1000.0      #A Floating Point
name = 'John'       # A string 

print(counter, end='\t')
print(type(counter))
print(miles, end='\t')
print(type(miles))
print(name, end='\t')
print(type(name))

# Multiple Assignment
a = b = c = 1
print('a'+' = ' +str(a)+ ', '+'b'+' = '+ str(b)+', and '+'c'+' = '+str(c))

a, b, c = 1, 2, 'john'
print('a'+' = '+str(a)+', '+'b'+' = '+str(b)+', and '+'c'+' = '+c)
