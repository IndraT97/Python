s = "egg"
t = "add"
dt = {}
dt2 = {}
if len(s) == len(t):
    for i,j in zip(s,t):
            if i in dt and dt.get(i) != j:
                print("Not an Isomorphic String")
                break
            else:
                dt.update({i:j})