import math


def find_avg_number():
    val = 0
    num = int(input('type any number \n'))
    for i in range(1, num + 1):
        val = val + i
    print(f'Avg of given range is {val // 2}')


def find_avg_input_number():
    num = int(input('type total number \n'))
    a = []
    for i in range(1, num + 1):
        elem = int(input('Enter elements \n'))
        a.append(elem)

    avg = sum(a) // 2
    print(f'Avg of Total input = {avg}')


def reverse_number():
    num = int(input('Enter any 3+ digit number\n'))  # 123
    val2 = num
    val = 0
    while num > 0:
        rem = num % 10
        val = val * 10 + rem
        num = num // 10
    print(f'Reverse of number {val2} is : {val}')


def sumof_digit():
    num = int(input('Enter any 3+ digit number\n'))  # 123
    val = 0
    while num > 0:
        rem = num % 10
        val = val +rem
        num = num // 10
    print(f'sum of total is {val}')

def check_Palindrome():
    num = int(input('Enter any 3+ digit number\n'))  # 123
    num_cpy = num
    val = 0
    while num > 0:
        rem = num % 10
        val = val * 10 + rem
        num = num //10
    if val == num_cpy : print('it\'s a Palindrome')
    else: print('It\'s not a Palindrome')


def count_digit():
    num = int(input('Enter any 3+ digit number\n'))  # 123
    val = 0
    while num > 0:
        val = val+1
        num = num // 10
    print(f'digits in given number is {val}')


def prime_num():
    num = 11

    # If given number is greater than 1
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")


if __name__ == '__main__':
    # find_avg_number()
    # find_avg_input_number()
    #reverse_number()
    #sumof_digit()
    #check_Palindrome()
    #count_digit()
    prime_num()