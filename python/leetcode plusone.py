
digits=[1,2,3]
x=[]
y=[]
for i in digits:
    i=str(i)
    x.append(i)
    res = int("".join(x))
    result=res+1
result=str(result)
for j in result:
    j=int(j)
    y.append(j)
print(y)


