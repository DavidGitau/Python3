import mysql.connector

# Multiple assignment
item1, item2,item3 = 1, 2, 4
x1 = x2 = x3 = x4 = 10

# Multi line Statements
total = item1 + \
        item2 + \
        item3
print(total)

# Find
name = "David Gitau Muruthi"
print(name.find('u'))

# Multiline quotation
paragraph = """This is a paragraph . It is 


made up of multiple lines and sentences and

can expand to any  line."""

print(paragraph)

# Waiting for the user
input('\n\nPress the ENTER key to continue')

# Multiple statements on a single line
import sys; x = 'foo'; sys.stdout.write(x+'\n')