# file_path = 'text_files/digits.txt'   ############## path to txt file


############################################### OPEN FILE AND PRINT AS OBJECT ALL CONTENTS #############
# with open(file_path) as file_object:
#     contents = file_object.read()

# print(contents)

############################################### OPEN FILE AND LOOP THROUGH LINE BY LINE ###############
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

############################################### OPEN FILE AND CREATE A LIST OF LINES FROM FILE ###########
# with open(file_path) as file_object:
#     lines = file_object.readlines() ################# READLINES METHOD STORES EACH LINE IN A LIST

# # for line in lines:
# #     print(line.rstrip())

# print(lines[2])    ################### ACCESS EACH LINE AS INDEX OF A LIST


###################################################### WRITE TO A TXT FILE. ONLY WRITES STRINGS OVERWRITES EVERYTHING IN FILE #################
# with open(file_path, 'w') as file_object:
#     file_object.write('I love it in here')

###################################################### APPENDING TO A FILE #############################

# with open(file_path, 'a') as file_object: ############################### 'a' appends instead of writes
#     file_object.write('\nI am ready for bed')
# file_path = 'text_files/guest.txt'

# while True:

#     users_name = input('What is your name?')
#     if users_name == 'quit':
#         break

#     print(f'Welcome {users_name}')
#     with open(file_path, 'a') as file_object:
#         file_object.write('\n' + users_name)
# try:
#     print(50/0)
# except ZeroDivisionError:
#     print('You cant divide by zero silly')

# def add_values(val1, val2):
#     return val1 + val2

# num_times = 0
# value1 = 0
# value2 = 0

# while num_times < 2:
#     prompt = input('please enter two values to add')
#     num_times += 1
#     if prompt == 'q':
#         break
#     elif num_times == 1:
#         try:
#             value1 = int(prompt)
#         except ValueError:
#             print('wrong type')
#             num_times -= 1
#     elif num_times == 2:
#         try:
#             value2 = int(prompt)
#         except ValueError:
#             print('wrong type')
#             num_times -= 1
#     elif value1 != 0 and value2 != 0:
#         continue
    

# try:
#     print(add_values(int(value1), int(value2)))
# except ValueError:
#     print('please enter a valid value from 0 - 9')
#     print('please try again')

# filenames = ['cats.txt', 'bags.txt', 'dogs.txt']

# def check_files(filename):
#     try:
#         with open(filename, 'r') as f:
#             contents = f.read()
#             print("\n" + contents)
#     except FileNotFoundError:
#         pass




# for filename in filenames:
#     check_files(filename)
    
# import json

# filename = "numbers.json"

# numbers = [2,4,6,3,12,45,76,23]

# with open(filename) as f:
#     json.load(f)

# print(numbers)
# filename = 'username.json'

# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input('what is your name')
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f'we will remember you next time {username}')
# else:
#     print(f'welcome back, {username}')        ###################### This block runs when "try" is successful

# filename = "favorite.json"

# # favorite_number = input('whats your favorite number')


# # with open(filename, 'w') as f:
# #     json.dump(favorite_number, f)

# try:
#     with open(filename) as f:
#         number = json.load(f)
# except FileNotFoundError:
#     print('file not found')
# else:
#     print(f'I know your favorite number, its {number}')


############################################################################# CH. 10 Check on learning ########################################################################
# filename = 'text_files/names.txt'

# with open(filename) as f:
#     contents = f.read()
#     print(contents)

# numbers = ['hello', 'my', 'name', 'is']

# with open(filename, 'a') as f:
#     for nums in numbers:
#         f.write('\n' + nums)


# import json

# filename = 'username.json'

# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     prompt = input('what is your username')
#     with open(filename, 'w') as f:
#         json.dump(prompt, f)
# else:
#     print(f'welcome back, {username}')




       


