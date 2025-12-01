n=int(input("num of pairs :" ))
d={}
for _ in range(n):
    key,value =input("enter key and value:").strip().split()
    d[key]=int(value)
ascending= sorted(d.items(),key=lambda x:x[1])
descending= sorted(d.items(),key=lambda x:x[1],reverse=True)
print("Ascending order:", ascending)
print("Descending order:", descending)
