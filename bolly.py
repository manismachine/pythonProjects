import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_proper_word():
    word = random.choice(words)
    while ' ' in word or '_' in word:
        word = random.choice(words)
    return word.upper()


def play_game():
    hidden_word = get_proper_word()
    word_letters = set(hidden_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        guess_word = [alphabet if alphabet in used_letters else '-' for alphabet in hidden_word]
        print(f'{guess_word} \n {lives_visual_dict[lives]}')
        user_input = input('Find hidden word by guessing any letter\n').upper()
        if user_input in alphabet:
            if user_input in used_letters:
                print(f'you have already used letter {user_input}')
            elif user_input in word_letters:
                used_letters.add(user_input)
                word_letters.remove(user_input)
                print('wow! guessed correct letter')
            else:
                used_letters.add(user_input)
                lives = lives - 1
                print(f'Sorry!, {lives} left ')
        else:
            print('Please enter proper alphabet')
    if lives > 0:
        print(f'Congrats. You guessed the word {hidden_word}')
    else:
        print(f'Ahh! you failed!, The Hidden word was {hidden_word}\n {lives_visual_dict[lives]}')


if __name__ == "__main__":
    play_game()
