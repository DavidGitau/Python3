import random

x = random.randint(1,6)
y = random.random()

print(f'x = {x}, y = {y}')

mylist = ['rock','scisors','paper']
z = random.choice(mylist)
print(z)

cards = [2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)