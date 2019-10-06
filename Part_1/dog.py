# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def sit(self):
#         print(f'{self.name} is sitting')


#     def roll_over(self):
#         print("%s is rolling over" % (self.name))


# my_dog = Dog('apple', 2)

# print(f'my dogs name is {my_dog.name}')
# print(f'My dogs age is {my_dog.age}')

# my_dog.sit()
# my_dog.roll_over()

# class Restruant:

#     def __init__(self, restruant_name, cuisine_type):
#         self.restruant_name = restruant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0


#     def describe_restruant(self):
#         print(f'{self.restruant_name.title()} is serving {self.cuisine_type}')


#     def restruant_open(self):
#         print(f'{self.restruant_name.title()} is open for business')


#     def set_num_served(self, number):
#         self.number_served = number


#     def increment_number_served(self, increment):
#         self.number_served += increment


# # new_restruant = Restruant('chilis', 'american')

# # # print(new_restruant.restruant_name)
# # # print(new_restruant.cuisine_type)

# # new_restruant.describe_restruant()
# # new_restruant.restruant_open()

# # res2 = Restruant('anabas', 'japanese')
# # res3 = Restruant('elchinos', 'mexican')

# # res2.describe_restruant()
# # res3.describe_restruant()
# new_restruant = Restruant('jockos', 'american')
# new_restruant.set_num_served(300)
# print(new_restruant.number_served)

# new_restruant.increment_number_served(500)
# print(new_restruant.number_served)

# class User:

#     def __init__(self, first_name, last_name, favorite_language):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.favorite_language = favorite_language
#         self.enrollment = True
#         self.login_attempts = 0


#     def is_enrolled(self, bool):
#         self.enrollment = bool


#     def describe_user(self):
#         if self.enrollment == True:

#             print(f"""This users name is {self.first_name.title()}
#             {self.last_name.title()}, their favorite language is
#             {self.favorite_language.title()} and they are currently enrolled""")
#         else:
#             print(f"""This users name is {self.first_name.title()}
#             {self.last_name.title()}, their favorite language is
#             {self.favorite_language.title()} and they are not enrolled""")


#     def greet_user(self):
#         print(f'Hello {self.first_name.title()} How is it going with {self.favorite_language.title()}')


#     def increment_login_attempts(self):
#         self.login_attempts += 1


#     def reset_login_attempts(self):
#         self.login_attempts = 0


# # user1 = User('nick', 'hartford', 'python')
# # user2 = User('amelia', 'hartford', 'java')
# # user2.enrollment = False
# # user3 = User('skyler', 'hart', 'c#')
# # user3.is_enrolled(False)



# # user1.describe_user()
# # user2.describe_user()
# # user3.describe_user()

# super_user = User('nick', 'hart', 'perl')

# super_user.increment_login_attempts()
# super_user.increment_login_attempts()
# super_user.increment_login_attempts()
# print(super_user.login_attempts)

# super_user.reset_login_attempts()
# print(super_user.login_attempts)



# class IceCreamStand(Restruant):

#     def __init__(self, restruant_name, cuisine_type):
#         super().__init__(restruant_name, cuisine_type)
#         self.flavors = ['chocolate', 'vanilla', 'strawberry']


#     def dispaly_flavors(self):
#         for flavor in self.flavors:
#             print(flavor)


# ics = IceCreamStand('mollys', 'ice cream')

# ics.dispaly_flavors()

# class Privileges:
#     def __init__(self):
#         self.privileges = ['add post', 'delete post', 'ban user']



#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege)



# class Admin(User):
#     def __init__(self, first_name, last_name, favorite_language):
#         super().__init__(first_name, last_name, favorite_language)
#         self.privilege = Privileges()






# new_admin = Admin('nick', 'hartford', 'django')
# # print(new_admin.first_name)
# new_admin.privilege.show_privileges()




# my_tesla = ElectricCar('Tesla', 'model s', 2019)
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()

