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

for i in sorted_st: print(i)