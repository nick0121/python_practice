from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        num = randint(1, self.sides)
        print(num)

new_die = Die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
print('\n')
die_2 = Die(10)
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()
die_2.roll_die()

print('\n')

die_3 = Die(20)
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()
die_3.roll_die()


