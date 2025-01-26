a = "11" 
b = "01"
output = "10101"
x=""
carry = 0

for i in range(len(a)):
    print(~i)
    if abs(~i) == len(a) and carry + int(a[~i]) + int(b[~i]) == 2:
        x = "10" + x
        print(x)
    else:
        if carry + int(a[~i]) + int(b[~i]) == 0 or carry + int(a[~i]) + int(b[~i]) == 1:
            x = f"{carry + int(a[~i]) + int(b[~i])}" + x
            carry = 0
            print(x)
        else:
            x = "0" + x
            carry = 1
            print(x)
x