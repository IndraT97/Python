x = "race a car"
y = ""
for i in x:
    if not i.isalnum():
        x = x.lower().replace(i,"")
    if i.isalnum():
        y = i.lower() + y 

if x == y:
    print("Yes, Plaindrome")
else:
    print("No")