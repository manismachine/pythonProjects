def swap_case(s):
    return s.swapcase()


def swap_case_typical(s):

    val =  [i.lower() if i.isupper() else i.upper() for i in s]
    return "".join (val)


if __name__ == '__main__':
    s = input()
    #result = swap_case(s)
    result = swap_case_typical(s)
    print(result)