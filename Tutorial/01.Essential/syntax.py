# Multi line Statements
import mysql.connector

item1, item2,item3 = 1, 2, 4
total = item1 + \
        item2 + \
        item3
print(total)

# Multiline quotation
paragraph = """This is a paragraph . It is 


made up of multiple lines and sentences and

can expand to any  line."""

print(paragraph)

# Waiting for the user
input('\n\nPress the ENTER key to continue')

# Multiple statements on a single line
import sys; x = 'foo'; sys.stdout.write(x+'\n')