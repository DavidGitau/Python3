student = ['Squidward','Sandy','Patrick','Spongebob','Mr. Krabs']
student.sort(reverse=True)

student_t = ('Squidward','Sandy','Patrick','Spongebob','Mr. Krabs')
sorted_s = sorted(student_t)

# for s in sorted_s: print(s)

students = [
    ('Squidward', 'F', 60),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 36),
    ('Spongebob', 'B', 20),
    ('Mr. Krabs', 'C', 78)
]
students_t = (
    ('Squidward', 'F', 60),
    ('Sandy', 'A', 33),
    ('Patrick', 'D', 36),
    ('Spongebob', 'B', 20),
    ('Mr. Krabs', 'C', 78)
)

age = lambda ages : ages[1]
students.sort(key=age)
sorted_st = sorted(students_t, key=age, reverse=True)

# for i in sorted_st: print(i)

# map() applies a func to each item in an iterable 
store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('jackets', 50.00),
    ('socks', 10.00)
]

to_euros = lambda data: (data[0],'{:.2f}'.format(data[1]*0.82))
to_dollars = lambda data: (data[0],'{:.2f}'.format(data[1]/0.82))

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

# for e in store_dollars: print(e)

# Filter function
age = lambda data: data[2] >= 35
old = list(filter(age,students))
for o in old: print(o)