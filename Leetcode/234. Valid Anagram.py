s = "rat"
t = "car"

if len(t) == len(s):
    for i in s:
        if s.count(i) == t.count(i):
            continue
        else:
            print("No Anagram")
            break