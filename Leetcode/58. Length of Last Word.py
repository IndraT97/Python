s = "   Hello, World!   "
for i in range(len(s)):
    if s.strip()[~i] ==" ":
        print(len(s[~i+1:len(s)]))
        break