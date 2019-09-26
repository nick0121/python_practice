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
# names = ['nick', 'juletta', 'skyler', 'amelia']

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
# names = ['nick', 'juletta', 'skyler', 'amelia']

# favorite_fruits = ['bananas', 'apples', 'pinapples']

# new_favorite_fruits = ['oranges', 'plums', 'apples']

# age = 12

# color = 'Purple'

# print(color == 'purple') # True
# print(color == 'Purple') # False

# print(color.lower() == 'purple') # True

# for name in names:
#     if name == 'nick':
#         print(f'I found {name}')
#     else:
#         print(f'{name}, is not nick')

# if 'nick' not in names:
#     print('this will not print')
# else: 
#     print('this will print')

# if 'juletta' in names:
#     print('this will print')
# else:
#     print('this will not print')

# for fruit in favorite_fruits:
#     if fruit in new_favorite_fruits:
#         print(f'You already said {fruit}')
#     else:
#         print(f'Adding new {fruit}')


######################################## CHAPTER 6: DICTIONARIES ###################################

# alien_0 = {'color': 'purple', 'points': 0}

# # accessing dictionary
# print(alien_0['color'])
# print(alien_0['points'])

# # Adding new key value pairs
# alien_0['x_position'] = 25
# alien_0['y_position'] = 50



# #  Changing valuse of key
# alien_0['color'] = 'green'


# # checking value in conditional
# alien_0['speed'] = 'medium'

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment 

# # Deleting key value pair
# del alien_0['y_position']

# # Get() Method
# get_value = alien_0.get('craft', 'this key does not exist') # returns second argument if the key does not exsist

# print(get_value)

# # create a dictionary of a  person I know
# person = {'f_name': 'juletta', 'l_name': 'juletta', 'age': 31, 'city': 'rockford'}

# # person_num = {
# #     'nick': 13,
# #     'juletta': 31,
# #     'skyler': 87,
# #     'amelia': 45
# # }

# # Looping through a dictionary
# for key, value in person.items():
#     print(key, value)


# # Loop through just the keys
# for name in person.keys():
#     print(name)

# for name in person:  # Same as above code. getting keys in default keys() method is not nessacary
#     print(name)

# # checking through list

# if 'erin' not in person.keys():
#     print('erin is not here')

# # Looping through in order
# # sorted() method
# for name in sorted(person.keys()):
#     print(name)

# # Looping through the values
# for name in person.values():
#     print(name)

# # set() method makes sure every value is unique
# for name in set(person.values()):
#     print(name)

# create a dictionary containing three major rivers
# rivers = {'tennessee river': 'united states', 'amazon river': 'south america', 'mississippi river': 'united states'}

# messages = ['The tennessee river runs through tennessee', 'the amazon river has piranah', 'the mississippi river has run backwards']


# for river in rivers:
#     if river == 'tennessee river':
#         message = messages[0]
#     elif river == 'amazon river':
#         message = messages[1]
#     else:
#         message = messages[2]

#     print(message)

# for name in rivers.values():
#     print(name)

# for name in set(rivers.values()):
#     print(f'\n{name}')

# for name in sorted(rivers.values()):
#     print(name)

#################################################### CHAPTER 6 CHECK ON LEARNING ###########################################

# names = {'first': 'nick', 'last': 'hartford'}

# print(names['first'])

# names['first'] = 'brian'

# print(names['first'])


# Get 
# first_name = names.get('first', 'key not found')

# Items 
# for name in names.items():
#     print(name)
# Keys 
# for name in names.keys():
#     print(name)
# Values
# for name in names.values():
#     print(name)

# if 'amelia' not in names.values():
#     print('amelia not forund')

# if 'nick' in names.values():
#     print('I found nick')

# for name in sorted(names.values()): 
#     print(name)

# List of dictionaries
# alien_0 = {'color': 'purple', 'station': 'earth'}
# alien_1 = {'color': 'green', 'station': 'mars'}
# alien_2 = {'color': 'red', 'station': 'venus'}
# alien_3 = {'color': 'blue', 'station': 'saturn'}

# aliens = [alien_0, alien_1, alien_2, alien_3]

# for alien in aliens:
#     print(alien)

# make a fleet of 30 aliens
# aliens = []

# for alien in range(30):
#     new_alien = {'color': 'purple', 'station': 'earth', 'points': 5}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'purple':
#         alien['color'] = 'gray'
#         alien['station'] = 'zenon'
#         alien['points'] = 25

# for alien in aliens[:5]:
#     print(alien)
# print('....')

# print(f'total number of aliens : {len(aliens)}')

# List inside a dictionary
# names = {'first': 'nick', 'suggested': ['tom', 'joe'], 'last': 'hart'}

# # Dictionary inside a dictionary
# dict_dict = {
#     'nhart': {'name': 'nick', 'last': 'hart'},
#     'ahart': {'name': 'amelia', 'last': 'hart'},
# }

# person_0 = {'name': 'nick', 'age': 33}
# person_1 = {'name': 'juletta', 'age': 31}
# person_2 = {'name': 'amelia', 'age': 3}

# people = [person_0, person_1, person_2]

# for person in people:
#     print(person)

#################################################### CHAPTER 7: USER INPUT AND WHILE LOOPS #################################
# message = input('please enter your name')

# print(message)
# message = input('what type of rental car would you like?')

# print(f'I see you selected a {message}')

# message = input('how many people will be joining us')

# if int(message) >= 8:
#     print('you will have to wait')
# else:
#     print('your table is ready')

# message = 'Please guess a number'
# message += '\nwhats your guess'

# new_message = input(message)

# if int(new_message) % 10 == 0:
#     print('yes')
# else:
#     print('no')

# WHILE LOOPS
# number = 1

# while number <= 10:
#     print(number)
#     number += 1

# message = ''

# while message != 'quit':
#     message = input('enter quit to end')
#     print(message)

# using a flag
# active = True
# while active:
#     message = input('enter quit to end')

#     if message == 'quit':
#         active = False
#     else:
#         print(message)
    

    # Using break to exit the loop
# while True:

#     message = input('enter quit')

#     if message == 'quit':
#         break
#     else:
#         print(message)

    # Using continue
# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
    
#     print(current_num)

#######################################Try it yourself
# while True:
#     prompt = 'enter your toppings'
#     prompt += '\ntype quit when done'

#     message = input(prompt)

#     if message == 'quit':
#         break
#     else: 
#         print('your selection will be added')

# prompt = 'how old are you'
# under_3 = 'Woohoo, you are free'
# under_12 = "you only pay 10 dollars"
# over_12 = "you pay the full price of 15 dollars"


# while True:
#     message = input(prompt)

#     if message == 'quit':
#         break
#     elif int(message) <= 3:
#         print(under_3)
#     elif int(message) > 3 and int(message) <= 12:
#         print(under_12)
#     else:
#         print(over_12)

# unconfirmed_users = ['alice', 'nick', 'sam']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f'verifying user: {current_user.title()}')
#     confirmed_users.append(current_user)

# print('the following have been confirmed')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# Deli
# sandwhich_orders =['tuna', 'blt', 'pbandj', 'pastrami', 'egg', 'pastrami', 'rye', 'pastrami']

# finished_sandwhiches = []

# print('no pastrami for you')

# while 'pastrami' in sandwhich_orders:
#     sandwhich_orders.remove('pastrami')

# while sandwhich_orders:
#     current_sandwhich = sandwhich_orders.pop()

#     print(f'Your {current_sandwhich} is being made')
#     finished_sandwhiches.append(current_sandwhich)

# for sandwhich in finished_sandwhiches:
#     print(sandwhich)


######################################################## CH. 7 CHECK ON LEARNING ##################################################

######################################################## CH. 8: FUNCTIONS #########################################################



