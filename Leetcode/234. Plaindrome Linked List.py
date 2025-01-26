head = [1,2,2,1]
for i in range(len(head) // 2):
    if head[i] == head[~i]:
        continue
    else:
        print("No")
        break