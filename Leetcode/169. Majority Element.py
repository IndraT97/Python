nums = [3,2,3]
dict = {}
x = ((len(nums))/2)
for i in nums:
    if i in dict.keys():
        dict[i] = dict.get(i) + 1
    else:
        dict.update({i:1})
if max(dict.values()) > x:
    print(max(dict, key=dict.get))
else:
    print("-1")