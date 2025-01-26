nums = [1,1,2,3,4,5,7,7,8,8,34,23,23]
for  i in nums:
    if i in nums[nums.index(i) + 1:]:
        nums.remove(i)
        print(nums)

# Wrong Approach