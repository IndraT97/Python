digits = [9]
x = ""
New_digit = []
for i in digits:
    x = x + str(i)
    y = int(x) + 1
for i in str(y):
    New_digit.append(int(i))
print(digits)
print(New_digit)