jewels = "aA"
stones = "aAAbbbb"
result=[]
for i in jewels:
     for j in stones:
         if i==j:
             result.append(i)
print(len(result))