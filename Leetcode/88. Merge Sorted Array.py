nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6] 
n = 3

for i in range(m):
    nums1[~i] = nums1[~i] + nums2[i]

print(nums1)

for i in range(len(nums1)):
    for y in range(0,len(nums1)-i-1):
        if nums1[y] > nums1[y + 1] :
            nums1[y] , nums1[y + 1] = nums1[y + 1] , nums1[y]
print(nums1)