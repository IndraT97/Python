n = 13
while n != 1:
    x = 0
    for i in str(n):
        x = x + int(i)**2
    n = x

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")