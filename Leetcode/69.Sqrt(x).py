x = 10
for i in range(0,100):
    if i*i == x:
        print(i)
        break
    elif i*i > x:
        print(i-1)
        break