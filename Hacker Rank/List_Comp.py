x = 1
y = 1
z = 2
n = 3

list1 = []
for i in range(x+1):
    for j in range(y+1):
            for k in range(z+1):
                if i+j+k != 3:
                    list1.append([i,j,k])
print(list1)