a=5
for i in range(a):
    if i==0 or i==a-1:   
        print("#"*a)
    else:
        x1=" "*(a-2)
        x2="#"+x1+"#"
        print(x2)
        
'''
a=4
sum=0
for i in range(a):
    sum+=1
    print("*"*sum)
    '''