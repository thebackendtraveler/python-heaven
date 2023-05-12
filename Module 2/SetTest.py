#!python3

#Define a set, and put fav foods in there
fav_food = {'burger', 'noodles', 'sausage', 'fries', 'milkshake'}

#A set that contains five fast foods from a friend
friend_food = {'burger', 'fries', 'cake', 'pie', 'churros'}

#Add a new item to the first set
fav_food.add('cookies')

#compare the lists
#The first shows what is not the same
print('Difference of fav food and friends food:', fav_food.difference(friend_food))

#The second shows what is the same in both lists
print('Same interests in fast food: ', fav_food.intersection(friend_food))

