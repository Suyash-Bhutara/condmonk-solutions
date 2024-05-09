def take_input():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = map(int, input().split())
        solve(A)

def solve(arr: list):
    height_hashmap = {}
    for i in arr:
        height_hashmap[i] = height_hashmap.get(i,0) + 1

    tuples_list = [(key, value) for key, value in height_hashmap.items()]
    sorted_tuples = sorted(tuples_list, key=lambda x: (x[1], x[0]))
    if sorted_tuples[-1][0] > sorted_tuples[0][0]:
        print(sorted_tuples[-1][1] - sorted_tuples[0][1])
    else:
        print(-1)

take_input()
