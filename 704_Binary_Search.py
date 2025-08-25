def binary_search(arr:list, target:int)->int:
    start, end = 0, len(arr)-1
    
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            end = mid+1
        elif arr[mid] > target:
            start = mid-1 
    return -1

arr = [3, 5, 1, 10, 20, 10, 12, 5]
arr.sort()
tar = 1
print(binary_search(arr, tar))
