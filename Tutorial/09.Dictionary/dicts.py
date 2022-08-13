# Changeable, unordered collection of unique key:value pairs. 
# Fast as they use hashing, allow us to access a value uniquely
# Immutable - can change them or alter when the program is running

"""
Mutable vs Immutable
There are two kind of types in Python. Immutable types and mutable types.
Immutables
An object of an immutable type cannot be changed. Any attempt to modify the object will result in a copy being
created.
This category includes: integers, floats, complex, strings, bytes, tuples, ranges and frozensets.

Mutables
An object of a mutable type can be changed, and it is changed in-situ. No implicit copies are done.
This category includes: lists, dictionaries, bytearrays and sets.

"""

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Kenya': 'Nairobi'
}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'New York'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['China'])
# print(capitals.get('Kenya'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items(): print(key, value)

