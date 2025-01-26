nums = [0,1,2,2,3,0,4,2]
list1 = []
list2 =[]
val = 2

for i in nums:
    if i == val:
        list2.append(i)
    else:
        list1.append(i)

lst = list1 + list2

print(lst)
print(list1)
print(list2)