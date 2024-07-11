string1 = "HackerRank.com presents Pythonist 2"
string2 = ''
for i in range(len(string1)):
    if string1[i] == string1[i].upper():
       string2 += string1[i].lower()
    else :
        string2 += string1[i].upper()
print(string1)
print(string2)