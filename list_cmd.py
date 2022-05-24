my_list = []

def execute_cmds(cmds):
    if (len(cmds) is 2):
        return my_list


if __name__ == '__main__':
    N = int(input())
    while N > 0:
        N = N - 1
        cmds = input().split()
        result = execute_cmds(cmds)
