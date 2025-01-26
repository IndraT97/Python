nums = [1,1,1,3,3,4,3,2,4,2]
for i in nums:
    if i in nums[nums.index(i) + 1:]:
        print("Contains Duplicate")
        break
else:
    print("No  Duplicate")

# using nums.index(i) is  not the correct approch