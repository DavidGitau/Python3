food = ['pizza','hamburger','hotdog','spaghetti','pudding']

food[0] = 'sushi'
food.append('ice cream')            # Add a new entry at the end of list
food.remove('sushi')                # removing item
food.pop()                          # remove the last item
food.insert(0,'cake')               # insert item in a given index
food.sort()
food.clear()                        # remove everything in the list

for i in food: print(i)

# 2D lists
drinks = ['coffee','soda','tea']
dinner = ['pizza','hamburger','hotdog']
dessert = ['cake','ice cream']

foods = [drinks,dinner,dessert]

print(foods[1][2])