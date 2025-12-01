n1=int (input("num of pairs in dict1: "))
d1={}
for i in range (n1):
    k,v= input("enter key and value: ").strip().split()
    d1[k]=v
n2=int (input("num of pairs in dict2: "))
d2={}
for i in range (n2):
    k,v= input("enter key and value: ").strip().split()
    d2[k]=v
d3={}
for k,v in d1.items():
  d3[k]=v
for k,v in d2.items():
   d3[k]=v
print("Merged dictionary:", d3)