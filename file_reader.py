file_path = 'text_files/digits.txt'   ############## path to txt file


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

    