haystack = "leetcode"
needle = "leeto"

for i in range(len(haystack)):
    for x in range(i+1,len(haystack)):
        if haystack[i:x] == needle:
            print(i)
            break
else:
    print(-1)