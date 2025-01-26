l = [2,3,5]
n = 14

for i in range(len(l)):
    for  j in range(i+1,len(l)):
        if l[i] * l[j] == n:
            print("Ugly Number")
            break
        elif any(l[i]**x == n for x in range(n)): 
                    print("Ugly")
                    break