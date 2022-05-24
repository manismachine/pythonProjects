# Guess the number
import random

user_number = 0
max_number = 10

def guess_the_number():
    global user_number
    system_number = random.randint(1, max_number)

    while system_number != user_number:
        user_number = int(input('Guess the number '))
        if user_number < system_number:
            print('your number is too low ')
        elif user_number> system_number:
            print('your number is too high')

    print(f'You guessed it correctly. your number is {system_number}')


def bot_guess_users_number():
    users_input = 'k'
    low = 1
    high = 10
    print('think of a number between 1 to 10, and bot will guess your number')

    while users_input != 'C':
        system_guessed_number = random.randint(low, high)
        users_input = input(
            f'if {system_guessed_number} is greater than your number enter [H] or if it is smaller than \ '
            f'your number type [L] or if bot guessed your number correct press [s]')
        if users_input == 'H':
            high = system_guessed_number-1
        elif users_input == 'L':
            low = system_guessed_number+1
        else: print('Please Dont Cheat')

if __name__ == '__main__':
    #guess_the_number()
    bot_guess_users_number()
