def find_uniq(arr):
    # your code here
    n = 0
    for i in arr:
        if i != arr[0]: 
            n=i
    if n!=arr[0] and arr[0]!=arr[1] and arr[0]!=arr[2]:
        n = arr[0]
    return n
