my_list = []
user_list = []

if __name__ == '__main__':
    N = int(input())
    # take total input number example 12
    while N > 0:
        N = N - 1
        #take each cmds and store cmds in list
        cmds = input().split()
        my_list.append(cmds)
    for i in my_list:
        #for every cmds take cmds and arguments list
        user_cmds = i[0]
        user_args = i[1:]
        if user_cmds != 'print':
            # eg:- you want to run 'user_list.insert(2,5)'
            # ctreate string same as comands eg: 'user_list.insert(2,5)' as string and pass to eval function
            user_cmds += "(" + ",".join(user_args) + ")"
            eval("user_list."+user_cmds)
        else:
            print(user_list)


# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print