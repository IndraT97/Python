head = [1,1,2,3,3]
lt = []
for i in head:
    if i not in lt:
        lt = lt + [i]
    else:
        continue
lt