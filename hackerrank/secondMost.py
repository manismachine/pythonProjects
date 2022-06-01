if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    oldarr = list(arr)
    oldarr2 = oldarr[:]
    max_old = max(oldarr)
    for i in oldarr2:
        # print(f'{i}\n')
        if max_old == i :
            oldarr.remove(i)

    print(max(oldarr))


# inputs
# 5
# 1 13 54 3 65