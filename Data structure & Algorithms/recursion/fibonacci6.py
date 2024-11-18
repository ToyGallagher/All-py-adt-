'''
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return (fibonacci(n-1) + (fibonacci(n-2)))

print(fibonacci(i),end = ' ')'''


def fibo(n):
    listnum = [1,1]
    for i in range(2,n):
       listnum.append(listnum[i-1] + listnum[i-2])
    return listnum[-1]

#print("fibo({n}) = {x}".format (n=n,x=fibo(n)))

n = int(input("Day: "))     
for i in range(1,n+1):
    print(fibo(i),end = ' ')