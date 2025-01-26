nums = [1]
dict = {}
for i in nums:
    if i in dict.keys():
        dict[i] = dict.get(i) + 1
    else:
        dict.update({i:1})
print(min(dict, key=dict.get))