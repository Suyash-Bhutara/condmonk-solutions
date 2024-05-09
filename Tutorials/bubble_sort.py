nums = [2,23,241,24,12,3,2,1,2,3,12,3,2,3,41,41,23]


def bubble_sort(arr: list, ascending: bool = True):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if ascending:
                if arr[j]>arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
            else:
                if arr[j]<arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
    return arr

print(bubble_sort(nums, ascending=False))