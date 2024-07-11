l = []
str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
for i in range(1,len(str)):
    l.append(max_width*i)
    if l[-1] > len(str):
        break
for i in reversed(l):
    str = str[:i] + '\n' + str[i:]
print(l)
print(str) 