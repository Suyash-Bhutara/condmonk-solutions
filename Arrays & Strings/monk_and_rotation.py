# array A of size N
# K: no of steps for right roration


def rotate_arr(arr: list, n: int, k:int):
    final_steps = k%n
    new_arr = arr[-1*final_steps:] + arr[:-1*final_steps]
    output_strings = [str(num) for num in new_arr]
    output_str = " ".join(output_strings)
    print(output_str)

def take_input():
    # Number of test cases
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        array = list(map(int, input().split()))
        rotate_arr(arr=array, n=N, k=K)

take_input()