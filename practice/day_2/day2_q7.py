n=int(input("num of tuples : " ))
result={}
for _ in range(n):
    k,v=input("enter key and value:").strip().split()
    if v.isdigit():
        v=int(v)
    result[k]=v
print("Dictionary:", result)