#1
'''
def printit(m, n):
    print(m,end = '')
    if m<n:
        printit(m+1,n)
        print(m,end='')
printit(3, 6)'''
#2
'''
def count_vowel(word):
    s=['a','e','i','o','u']
    if len(word)>0:
        if word[0].lower() in s:
            out=1
        else:
            out=0
    else:
        return 0
    return out+count_vowel(word[1:])'''
#4
'''
def count(word,ch,result):
    if len(word)==0:
        return 0
    if ch is word[0]:
        hit=1
    else:
        hit=0
    return hit+count(word[1:],ch,result)

word=input()
ch=input()
print(count(word,ch,0))'''
#5
'''
def divnums(n,d):
    s = ''
    if n==0:
        return ''
    if n%d == 0:
        s='{} '.format(n)
    return divnums(n-1,d)+s
print(divnums(10, 3))'''
#7
'''
def is_palindrome(word):
    if len(word)==0 or len(word)==1:
        return True
    elif word[0]==word[-1]:
        p=True
    else:
        p=False
    return p and is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('redder')) '''
#8 
'''
def count_even(lst):
    if len(lst)==0:
        return 0
    if lst[0]%2==0:
        even=1
    else:
        even=0
    return even+count_even(lst[1:])

print(count_even([1,2,3,5,2,2,10]))'''
#9
'''
def in_list(lst,x):
    if len(lst)==0:
        return False
    if lst[0] is x:
        return True
    return False or in_list(lst[1:],x)'''
#10


#11
'''
def sum_square(n):
    if n==0:
        return 0
    else:
        total = n**2
    return total+sum_square(n-1)'''
#14
'''
def power(n,k):
    if k==0:
        return 1
    return n*power(n,k-1)'''
#15
'''
def flatten_list(lst):
    if len(lst)==0:
        return []
    if isinstance(lst[0],list):
        flst=flatten_list(lst[0])
    else:
        flst=[lst[0]]
    return flst+flatten_list(lst[1:])
'''



'''
for i in range(10,22,3):
    print(i)'''

'''
PASSWORD = "I love Python"

s = input("Enter password: ")
while s != PASSWORD:
    print("Incorrect password.  Access denied.")
    s = input("Enter password: ")

print("Correct password.  Access granted.")'''
'''
numpos = []
numneg = []
while True:
    num = float(input("Enter a number (or 0 to exit): "))
    if num>0:
        numpos.append(num)
    elif num<0:
        numneg.append(num)
    elif num == 0:
        break
print(f"The sum of all positive numbers is {sum(numpos):.2f}")
print(f"The sum of all negative numbers is {sum(numneg):.2f}")
'''
'''
from turtlelab8 import turtle,radar,check

# Put your turtle movement commands here
bp = radar.ball_direction()
while bp != 'x':
    if bp[0] == 'n':
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        bp = radar.ball_direction()
    if bp[0] == 's':
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        bp = radar.ball_direction()
    if (bp[0] or bp[1]) == 'e':
        turtle.forward(20)
        bp = radar.ball_direction()
    if (bp[0] or bp[1] == 'w'):
        turtle.left(180)
        turtle.forward(20)
        turtle.right(180)
        bp = radar.ball_direction()
check()
'''

