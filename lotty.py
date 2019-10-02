from random import choice



numbers = [10, 12, 3, 45, 26, 65, 29]
attepmts = 0
guesses = 0
winner = [12, 3, 26, 10]
guess = []

while True:

    while attepmts < 4:

        guess.append(choice(numbers))
        attepmts += 1


    print(guess)

    # print(sorted(guess))

    if sorted(winner) == sorted(guess):
        print('Winner, Winner chicken dinner')
        guesses += 1
        break
    else:
        guesses += 1
        guess = []
        attepmts = 0
        

print(guesses)






