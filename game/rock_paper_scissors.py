import random
# r>s, s>p, p>r

def play(player, opponent):
    if user_input == computer_input:
        return print('It\'s a tie !!')
    elif is_win(user_input, computer_input):
        return print(f'you won . computers guess was {computer_input}')
    return print('you lost computer choice is vinti')


def is_win(user_input,computer_input):
    if (user_input == 'r' and computer_input == 's') or (user_input == 's' and computer_input == 'p') or (user_input == 'p' and computer_input == 'r' ):
        return True


if __name__ == '__main__':
    user_input = input("Whats your choice? Type 'r' for rock, 'p' for paper and 's' for scissiors \n")
    computer_input = random.choice(['r', 'p', 's'])

    play(user_input, computer_input)
