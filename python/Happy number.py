num=19
result=0
while num>0:
    r=num %10   
    result+=r**2
    num=num//10
print(result)


'''
sum(y)==1:
    if sum(y)==1:
        x = [int(a) for a in str(num)]
        for i in x:
            i=i**2
            y.append(i)
    #print(y)
            print(sum(y))
            print(True)
    else:
        print(False)
   
'''




#y=[]
#for i in range(len(x)):
#    y.append(index(i))
#print(y)