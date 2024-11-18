num = 11
x = [int(a) for a in str(num)]
result1=x[0]+x[-1]
y = [int(b) for b in str(result1)]
result2=y[0]+y[-1]

if len(x)==1 :
    print(num)
elif x[-1]==0:
    print(x[0])
elif x[0]==x[-1]:
    print(x[0]+x[-1])

else:
    print(result2)

