x = 0
l = []

while len(str(x)) > 1:

        for i in str(x):
            l.append(int(i))
        x = sum(l)
        l = []
x