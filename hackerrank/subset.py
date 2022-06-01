results = []


def find_subset():
    test_cases = int(input())
    while test_cases > 0:
        test_cases = test_cases - 1

        digit_a = int(input())
        a = set(input().split())

        digit_b = int(input())
        b = set(input().split())

        if a.issubset(b):
            results.append(True)
        else:
            results.append(False)

    for val in results:
        print(val)


if __name__ == '__main__':
    find_subset()



#