# message = "Hello!"


# secMessage = "Nick"

# print(f"{message}{secMessage}")

# message = "Hello nick, would you like to learn some python today?"

# print(message)

# pName = "nick"

# print(pName.title())
# print(pName.upper())
# print(pName.lower())

# famous_person = " henry ford "

# quote = f'{famous_person.title().strip()} once said, "Whether you think you\n\t can or you think you cant, your right"'

# print(quote)

# print(5+3)
# print(4*2)
# print(16/2)
# print(10-2)


####################################################################LISTS####################################################################
# games = ['borderlands', 'call of duty', 'battlefield']

# print(games[0])

# for game in games:
#     print(game)
# games.append('assasins creed')

# games.insert(0, 'titanfall')

# for game in games:
#     print(game)

# games.append('tomb raider')
# print('')

# del games[2]
# print('')


# rmGame = games.pop()

# for game in games:
#     print(game)
# print('')
# print(rmGame)

# games.remove('borderlands')
# print('')
# games.append('fallout')

# for game in games: 
#     print(game)

# names = ['nikola tesla', 'elon musk', 'carl jueng']

# not_coming = 'carl jueng'
# names.remove(not_coming)

# for name in names:
#     print(f'Hello, {name.title()} you are invited to dinner')

# print('')
# # add a print message at the end with the names of the people that cant make it.
# print(f'These people are not coming: {not_coming}')

# # Replace the person who cant make it with another person
# names.append('bill gates')

# print('good news, we found a bigger table')

# names.insert(0, 'edgar allen poe')
# names.insert(2, 'steve jobs')
# names.append('warren buffet')


# print('')

# rm_names = names.pop()
# print(f'I am sorry {rm_names} you are no longer invited')

# rm_names = names.pop()
# print(f'I am sorry {rm_names} you are no longer invited')

# rm_names = names.pop()
# print(f'I am sorry {rm_names} you are no longer invited')

# rm_names = names.pop()
# print(f'I am sorry {rm_names} you are no longer invited')


# # print invitations with new list
# for name in names:
#     print(f'Hello, {name.title()} you are invited to dinner')

# print('')

# del names[0]
# del names[0]

# print(names)


# Store 5 places you would like to visit in a list
# places = ['japan', 'tailand', 'germany', 'brazil', 'greece']

# print(places)

# # Print a sorted list alphabetically
# print(sorted(places))
# print(places)

# print(sorted(places, reverse=True))

# print(places)

# places.reverse()

# print(places)

# places.reverse()

# print(places)

# places.sort()
# print(places)

# places.sort(reverse=True)
# print(places)
# print(len(places))

# cities = ['maryville', 'knoxville', 'rockford', 'alcoa', 'farragut']

# # Print list at index number
# print(f'I live in {cities[2]}')
# # Append 
# cities.append('townsend')
# print(cities)
# # Insert 
# cities.insert(3, 'friendsville')
# print(cities)
# # Delete
# del cities[1]
# print(cities)
# # Pop 
# cities.pop()
# print(cities)
# # Remove by name
# cities.remove('farragut')
# print(cities)
# # Sort
# print(sorted(cities))
# # Reverse sort
# print(sorted(cities, reverse=True))
# # Sorted
# cities.sort()
# print(cities)
# # Reverse sorted
# cities.sort(reverse=True)
# # Get length
# print(len(cities))

###################################################WORKING WITH LISTS CH. 4######################################################
# games = ['tomb raider', 'borderlands', 'titan', 'call of duty', 'forza']

# for game in games:
#     print(game)

# pizzas = ['pepperoni', 'sausage', 'cheese']

# for pizza in pizzas:
#     print(f'I like {pizza} pizzas')

# animals = ['cats', 'dogs', 'tigers']

# for animal in animals:
#     print(f'I think {animal} would make a good pet!')

# for value in range(1, 21):
#     print(value)

# numbers = []

# for value in range(1, 1000001):
#     numbers.append(value)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for value in range(1, 11):
#     print(value**3)

# cubes = [value**3 for value in range(1,11)]
# print(cubes)


# names = ['Nick', 'juletta', 'skyler', 'amelia', 'apple', 'gipsy']

# # print(names[3:5])
# ############################## Copying a list

# names.append('joe')
# names.append('bill')
# names.append('suzy')
# # print(names)
# # print(len(names))

# print(f'This is the first three names {names[:3]}')
# print(f'This is the middle three names {names[3:6]}')
# print(f'This is the last three names {names[6:]}')

# pizzas = ['pepperoni', 'sausage', 'cheese']

# friends_pizzas = pizzas[:]

# pizzas.append('salomi')
# friends_pizzas.append('artichoke')

# for pizza in pizzas:
#     print(pizza)

# for item in friends_pizzas:
#     print(item)

############################TUPLES 
# dimensions = (20,50)

# for dim in dimensions:
#     print(dim)

# dimensions = (50, 35)

# for dim in dimensions:
#     print(dim)
# foods = ('pizza', 'cheeseburger', 'pie', 'grilled cheese', 'tacos')

# # foods.append('toast')############Does not work. Can not assign a new item to tuple

# print(foods)

# foods = ('pizza', 'cheeseburger', 'pie', 'grilled cheese', 'tacos', 'chili')

# print(foods)
