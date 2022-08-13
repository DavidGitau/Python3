# Collection which is unordered, unindexed and no duplicate values

utensils = {'fork','spoon','knife','knife'}
dishes = {'bowl','plate','cup','knife'}

utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()

# utensils.update(dishes)

dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
print(utensils.intersection(dishes))

# for x in utensils: print(x)