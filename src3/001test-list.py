food = ['hotdog', 'pizza']
food.append('beer')
food.insert(2, 'Mineirin')
print(food)
food_copy = food[:]
print('copiei...')
food.sort(reverse=True)
print(food)
del food[0]

print(food)

food.pop()

print(food)
print(food_copy)