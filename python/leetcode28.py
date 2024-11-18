haystack = "aaaaa"

needle = "bba"

x=""
y=""
for i in haystack:
    x+=i
for j in needle:
    if j in x:
         y+=j
print(haystack.index(y))