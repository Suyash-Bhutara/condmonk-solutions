###########################
# Approach 1
###########################

# def take_input():
#     N = int(input())
#     A = []
#     for _ in range(N):
#         A.append(input())
#     solve(A)

# def solve(arr: list):
#     for i in range(len(arr)):
#         cnt = 0
#         for j in range(i):
#             if arr[j] < arr[i]:
#                 cnt+=1
#         print(cnt)

# take_input()


###########################
# Approach 2
###########################
def take_input():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
        cnt = 0
        for j in range(i):
            if A[j] < A[i]:
                cnt+=1
        print(cnt)

take_input()