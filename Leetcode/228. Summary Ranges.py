nums = [0,1,2,3,6,7,8,9,11,12]
x = [nums[0]]
z = []
n = 0
for i in range(n,len(nums)-1):
    if nums[i+1] - nums[i] == 1:
        x = x + [nums[i+1]]
    else:
        z.append(x)
        x = [nums[i+1]]
        n = i

z.append(x)