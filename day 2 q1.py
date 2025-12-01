def second_largest(nums):
    max1=max2=None
    for n in nums:
        if max1 is None or n>max1:
            max2=max1
            max1=n
        elif n != max1 and (max2 is None or n>max2):
            max2=n
    return max2
n= int(input("nummber of elements: "))
arr= list(map(int, input().strip().split()))
result = second_largest(arr)
if result is None:
    print("No second largest element")
else :
    print("The second largest element is:", result)

