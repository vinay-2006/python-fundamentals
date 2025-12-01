def remove_duplicates(arr):
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
n= int(input("number of elements: "))
arr= list(map(int, input().strip().split()))
result = remove_duplicates(arr)
print("Array after removing duplicates:", ' '.join(map(str, result)))