n=int(input("num of pairs in dict1: " ))
l=list(map(int,input("enter elements:").strip().split()))
reversed_arr=l[::-1]
print("Reversed array:", ' '.join(map(str, reversed_arr)))
