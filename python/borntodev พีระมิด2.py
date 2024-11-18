'''
def pyramid(k):
    for i in range(k):
        print(" "*(k-i-1)+"*"*((2*i)+1))
pyramid(4) 
'''
num = int(input())
for i in range(num):
    print(" "*(num-i-1),"/")
    print("")