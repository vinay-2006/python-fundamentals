import json
def nested_lookup(dct, keys):
    cur = dct
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    return cur


n=int(input().strip())
path =input().strip()
raw_dict=input().strip().split()
data =json.loads(raw_dict)
result= nested_lookup(data, path)
if result is None :
    print("Path not found")
else :
    print("Value at path:", result)
    