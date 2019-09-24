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

#################################### CHECK ON LEARTNING: LISTS

# games = ['titanfall', 'assassins creed', 'fallout', 'battlefield', 'borderlands'] # List#########################

# dimensions = (300, 500)        #Tuple###########################

# # Access list at index
# print(games[2]) #should print fallout
# # add to list 
# games.append('tron')
# # print(games)
# # insert into list at index
# games.insert(4, 'forza')
# print(games)
# # remove from list
# rmGame = games.pop()
# print(games)
# # remove from front of list
# games.remove('fallout')
# print(games)
# # delete item
# # del games[0]
# # print(games)
# # use removed item
# print(f'{rmGame} was removed from list of games')
# # sort #################permanetly sorts list
# # games.sort()
# # print(games)
# # # reverse sort
# # games.sort(reverse=True)
# # print(games)
# # sorted ######################### creates copy of sorted list
# print(sorted(games))
# # reverse sorted
# print(sorted(games, reverse=True))
# # range
# numbers = []

# for value in range(1, 21):
#     numbers.append(value)

# print(numbers)
# # min 
# print(min(numbers))
# # max 
# print(max(numbers))
# # sum
# print(sum(numbers))
# # slice
# print(numbers[3:]) # prints from 3rd index to end of current list
# print(numbers[-3:]) # prints last 3 indexes no matter how long list gets
# print(numbers[2:5])

# # copy a list 
# newGames = games[:] # must use : or index numbers and : # if not new list will only reference old list not create new list

# games.append('grand')
# print(games)

# newGames.append('wormland')
# print(newGames)


############################################## CHAPTER 5: Conditionals ################################################
names = ['nick', 'juletta', 'skyler', 'amelia']

# # if names[1] == 'juletta':
# #     print('that is correct syntax')

# # num = 18

# # if num < 20 or num > 12: 
# #     print('this is true')
# user = 'apple'

# if user not in names:
#     print(f'{user} not found')

# names.append('apple')

# if user in names:
#     print(f'{user} was found')
# car = 'mazda'
# print(f'Is car = {car}, I predict true')
# print(car == 'mazda')

# name = 'Shelby'

# # if name not in names:
# #     print(f'{name} not found')
# print(name != 'shelby') # Evaluates to true
# print(name.lower() != 'shelby') # Evaluates to false

# x = 12 

# if x == 12:
#     print('this is true')

# print(12 < 18 and 13 > 20) # False condition

# for name in names:
#     if name == 'nick':
#         print('nick')
#     else:
#         print('not nick')

# if 'nick' in names:
#     print('I found you')

# age = 18 

# # if age < 21:
# #     message = 'you are too young'

# # print(message)
# if age < 4:
#     price = 0
# elif age <= 18:
#     price = 25
# elif age <= 40:
#     price = 50

# print(f'your cost is {price}')
# alien_color = 'red'

# if alien_color == 'green':
#     print('YOu earned 5 points')
# elif alien_color == 'yellow':
#     print('you just earned yourself 10 points')
# else:
#     print('ypu earned the most points')

# age = 33

# if age <= 2:
#     print('you are a baby')
# elif age > 2 and age <= 4:
#     print('you are a toddler')
# elif age > 4 and age <= 13:
#     print('you are a kid')
# elif age > 13 and age <= 20:
#     print('you are a teen')
# elif age > 20 and age <= 65:
#     print('you are an adult')
# elif age > 65:
#     print('you are an elder')

# favorite_fruits = ['bananas', 'apples', 'pinapples']

# if 'apples' in favorite_fruits:
#     print('You really like apples')
# if 'bananas' in favorite_fruits:
#     print('You really like bananas ')

# usernames = ['hjuletta', 'nhartford', 'skylerBear', 'warriorPrincess']

# new_usernames = ['count_dracula', 'drPepper', 'hJuletta', "SKYLERBEAR"]

# lower_usernames = []

# for user in new_usernames:
#     lower_usernames.append(user.lower())

# for user in usernames:
#     if user.lower() in lower_usernames:
#         print('That name is not available')
#     else:
#         print(f'{user}, is available')

# usernames.insert(2, 'admin')

# for user in usernames:
#     if user == 'admin':
#         print(f'{user}, welcome master')
#     else:
#         print(f'{user}, hello slave')

# numbers = []

# for nums in range(1, 10):
#     numbers.append(nums)

# print(numbers)

# for nums in numbers:
#     if nums == 1:
#         print(f'\n{nums}st')
#     elif nums == 2:
#         print(f'\n{nums}nd')
#     elif nums == 3:
#         print(f'\n{nums}rd')
#     else:
#         print(f'\n{nums}th')

######################################## CHAPTER 5 CHECK ON LEARNING ###############################

######################################## CHAPTER 6: DICTIONARIES ###################################