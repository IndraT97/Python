L = [[5,"Harry"],[37.21,"Berry"],[37.2,"Tina"],[41,"Akriti"],[39,"Harsh"]]

list1 = []
list2 = []
for i in range(len(L)):
    list1.append(L[i][0])
    list1.sort()

for m in L:
    if m[0] == list1[-2]:
        list2.append(m[1])
        list2.sort()

print(list2)