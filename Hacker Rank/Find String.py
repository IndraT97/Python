str1 = "ABCDCDC"
str2 = "CDC"
list3 = []
for i in range(len(str1) - len(str2) + 1):
    if str1[i:i+3] == str2:
       list3  += [1]