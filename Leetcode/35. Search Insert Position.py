nums = [1,3,5,6] 
target = 7
for i in nums:
    if i == target:
        print(nums.index(i))
        break
    else:
        k = sorted(nums + [target])
        print(k.index(target))
        break