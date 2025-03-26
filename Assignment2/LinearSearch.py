def linear_search(arr ,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr=[3,8,7,0,2,4,5,1,6]
target = 4

result = linear_search(arr,target)

if result != -1:
    print(f"Target number is at {result}th index.")
else:
    print("Target not found")
