
head = [1,2,3,4,5]
head2 = []
for i in range(len(head)):
    head2.append(head[~i])

#S2--

head = [1,2,3,4,5]
for i in range(len(head) // 2):
        print(i,~i)
        head[i],head[~i] = head[~i],head[i]
head