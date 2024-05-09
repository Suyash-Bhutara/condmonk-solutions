def take_input():
    string, k = map(str, input().split())
    suffix_list = []
    for i in range(len(string)):
        suffix_list.append(string[i:])
    suffix_list.sort()
    print(suffix_list[int(k)-1])

take_input()



