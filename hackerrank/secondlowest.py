if __name__ == '__main__':
    # score_list = [['a', -50], ['b', -50], ['c', -50], ['d', 51]]
    # score_list = [['a', 20], ['b', 20], ['c', 19], ['d', 19], ['e', 21]]
    values = []

    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])

for inner in score_list:
    values.append(inner[1])

values = set(values)
minimum = min(set(values))
values.remove(minimum)
new_minimum = min(values)
# print(f'Second lowest is : {new_minimum}')

for inner in sorted(score_list):
    if (inner[1] == new_minimum):
        print(inner[0])
