def create_pattern(param):
    for i in range(param):
        total = param+2
        print(' '*(param-(i+1))+'*'*(i+1)+' '*(param-(i+1)))


if __name__ == '__main__':
    create_pattern(5)