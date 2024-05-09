# input matrix NxN

def mat_inv(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            for k in range(i, len(arr)):
                for l in range(j, len(arr[0])):
                    if arr[i][j]>arr[k][l]:
                        count +=1
    
    print(count)

def take_input():
    # Number of test cases
    T = int(input())
    for _ in range(T):
        N = int(input())
        matrix = []

        for _ in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        
        mat_inv(matrix)

take_input()