## change string(string is immutable like tupple, but list are mutable so we will convert
# string or tupple into list , we will change and then convert back to uriginal type)

def mutate_string(string, position, character):
    list_val = list(string)
    val = list_val[position] = character
    return ''.join(list_val)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)