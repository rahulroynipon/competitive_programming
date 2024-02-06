def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # Sort the array

for _ in range(q):
    num = int(input())
    print('found' if binary_search(arr, num) else 'not found')
