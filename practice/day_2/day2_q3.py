from collections import Counter
n = int(input("number of elements: "))
arr = list(map(int, input("enter elements:").strip().split()))
freq = Counter(arr)
for k,v in freq.items():
    print(f"Element {k} occurs {v} times")