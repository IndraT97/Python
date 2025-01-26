nums = [1,0,1,1]
k = 1
for i in range(len(nums)):
    for j in range(i+1 ,len(nums)):
        if nums[i] == nums[j] and abs(i-j) <= k:
           print("True")
           break