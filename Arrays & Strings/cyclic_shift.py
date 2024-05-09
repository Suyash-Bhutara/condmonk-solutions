# Medium Difficulty

def take_input():
    T = int(input())
    for _ in range(T):
        N,K = map(int, input().split())
        string = input()
        solve(N,K, string)

def solve(n: int, k: int, string: str):
    # max string
    max = ""
    # distance to max string
    d = 0
    # periodicity to reach max string
    p = -1

    for i in range(len(string)):
        if max < string:
            max = string
            d = i
        elif max == string:
            p = i - d
            break
        string = string[1:] + string[0]
    
    if p ==-1:
        print(d + (k-1)*n)
    else:
        print(d + (k-1)*p)

take_input()