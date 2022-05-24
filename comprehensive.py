import math


def do_the_trick(x, y, z, n):
    val = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n]
    print(val)


if __name__ == '__main__':
    x = int(input('enter x\n'))
    y = int(input('enter y\n'))
    z = int(input('enter z\n'))
    n = int(input('enter n\n'))

    do_the_trick(x, y, z, n)