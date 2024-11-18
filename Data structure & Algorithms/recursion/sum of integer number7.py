def sumdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumdigits(int(n/10))
print(sumdigits(678))
print(sumdigits(79))
        

#อีกวิธี
'''
x=678
x=str(x)
sum=0
for i in x:
    i=int(i)
    sum+=i
print(sum)
'''