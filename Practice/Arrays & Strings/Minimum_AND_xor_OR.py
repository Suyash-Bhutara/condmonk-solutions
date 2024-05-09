# (A AND B) xor (A OR B) = A xor B (can be solved using identities)
def take_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input()
        A = [int(i) for i in A.split(" ")]
        solve(N, A)

def solve(n: int, A: list):
    A.sort()
    min_val = float('inf')
    for i in range(len(A)-1):
        xor_val = A[i]^A[i+1]
        if xor_val < min_val:
            min_val = xor_val
    
    print(min_val)

take_input()