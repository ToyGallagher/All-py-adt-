#1
'''
def isPrime(number):
    """
    Check if the number is prime number
    :params number: is the number to check if is prime number
    :return: True if the number is prime number
             False if the number isn't prime number
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(1231)
    True
    >>> isPrime(14)
    False
    """
    if number>=1:
        for i in range(2,number):
            if number%i == 0 :
                return False
        return True

def printAllPrimes(limit):
    """
    Print all the prime number between 1 to the limit
    >>> printAllPrimes(10)
    2 3 5 7
    >>> printAllPrimes(20)
    2 3 5 7 11 13 17 19
    >>> printAllPrimes(0)

    >>> printAllPrimes(2)
    2
    >>> printAllPrimes(3)
    2 3
    """
    for i in range(2,number+1):
        if isPrime(i) == True:
            print(i,end = ' ')

number = int(input("Input n: "))
printAllPrimes(number)
'''

#1.5
'''
def list_factors(n):
   """
   Get string of factors of n
   :params n is an integer to find factors
   :return string of factors (with a space between each factor)
   >>> list_factors(6)
   '1 2 3 6 '
   >>> list_factors(7)
   '1 7 '
   >>> list_factors(12)
   '1 2 3 4 6 12 '
   """
   result_factors = ""
   for i in range(1,n+1):
        if n%i == 0:
            result_factors += f"{i} "
   return result_factors

def find_sum_and_num_factors(n):
   """
   Find summation and count number of factors of n
   :params n is an integer to find factors
   :return sum is summation of factors of n
           count is number of factors of n
   >>> find_sum_and_num_factors(6)
   (12, 4)
   >>> find_sum_and_num_factors(7)
   (8, 2)
   >>> find_sum_and_num_factors(12)
   (28, 6)
   """
   
   sum = 0
   n = n.split()
   for i in n:
    i = int(i)
    sum += i 
   numfac = len(n)
   return sum,numfac

number = int(input("Enter positive number: "))
print(f"Factors of {number} are")
n = list_factors(number)
sumnum,numfac = find_sum_and_num_factors(n)
print(n)
print(f"Sum of {n}is {sumnum}")
print(f"Number of factors is {numfac}")
for i in range(2,number):
    if number%i==0:
        print(f"{number} is not prime number.")
        break
    else:
        print(f"{number} is prime number.")
        break
'''

#2
'''
def tree(n):
    for i in range(1,n+1):
        print(" "*(n-i),end = '')
        print("*"*(2*i-1))

x = int(input("How many levels? "))
n = int(input("Enter bush size: "))
for i in range(x):
    tree(n)
'''
#3
'''
x = int(input("input: "))
for i in range(1,(x//2)+2):
    print(" "*((x//2+1)-i),end = '')
    print("#"*(2*i-1))
for i in range(1,(x//2)+1):
    print(" "*(i),end = '')
    print("#"*((x)-(2*i)))
'''
#4
'''
def trophy(n):
    count = n*2+3
    for i in range(n):  # 0,1,2
        print(" "*(i)+"="*(count)) 
        print(" "*(i)+"="+"#"*(count-2)+"=")
        count = count-2
    count = 1
    for i in range(n//2): 
        print(" "*(n-i+1)+"="*count)
        print(" "*(n-i)+"="+"#"*(count)+"=")
        count = count+2

n = int(input("n: "))
trophy(n)
'''
#5
'''
def hammer(n):


n = float(input("Input Gold: "))
hammerlevel = int(n//1000)
'''
#6
'''
def totalday(day,month,day_in_month):
    result = day
    for i in range(1,month):
        result += day_in_month[i]
    return result
day = int(input("d: "))
month = int(input("m: "))
year = int(input("y: "))
if (year%4 == 0 and year %100!=0) or year%400 == 0:
    i=1
else:
    i=0
day_in_month = {1:31, 2:28+i, 3:31,
               4:30, 5:31, 6:30,
               7:31, 8:31, 9:30,
               10:31, 11:30, 12:31}
result = totalday(day, month,day_in_month)
print(result)               
'''
#7
'''
def top_part(n):
    count = 2+3*(n-2)
    for i in range(n-1):
        print(" "*i+"*"+" "*count+"*")
        count = count-2
def mid_part(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print(" "*(n-1)+"*"*n)
        else:
            print(" "*(n-1)+"*"+" "*(n-2)+"*")
def bottom_part(n):
    count = n
    for i in range(n-1):
        print(" "*(n-i-2)+"*"+" "*(count)+"*")
        count+=2

def draw(n):
    top_part(n)
    mid_part(n)
    bottom_part(n)
n = int(input())
draw(n)
'''
'''
n = int(input())
count = 4+3*(n-2)-2
for i in range(n-1):
    print(" "*i+"*"+" "*count+"*")
    count = count-2
for i in range(n):
    if i == 0 or i ==n-1:
        print(" "*(n-1)+"*"*n)
    else:
        print(" "*(n-1)+"*"+" "*(n-2)+"*")
count = n
for i in range(n-1):
    print(" "*(n-i-2)+"*"+" "*(count)+"*")
    count+=2

    '''

#8
'''
def draw(inputlist):
    for i in range(len(inputlist)):
        print(inputlist[i]*(i+1))
while True:
    inputnumber = input()
    inputlist = inputnumber.split()
    if inputlist[0] == "0":
        print("Good Bye.")
        break
    else:
        draw(inputlist)
'''

#9
'''
datalist = list(map(int, input().split()))
while True:
    menu,x = input().split()
    x= int(x)
    if menu == "A":
        datalist.append(x)
    elif menu == "S":
        print(datalist[x])
    elif menu == "R":
        datalist.remove(datalist[x])
    elif menu == "E":
        break
for i in range(len(datalist)):
    print(datalist[i],'',end='')
'''
#10
'''
lucky = input("Enter lucky number : ")
candidate = int(input("Enter amount of candidates : "))
listid = []
countlucky = []
for i in range(candidate):
    id = input(f"Enter ID card number {i+1}: ")
    listid.append(int(id))

for i in range(len(listid)):
    listid[i] = str(listid[i]) 

for i in range(len(listid)):
    count = listid[i].count(lucky)
    countlucky.append(count)

index = countlucky.index(max(countlucky))
luckyid = listid[index]
for i in range(candidate): 
    if countlucky[i] == max(countlucky) and listid[i]>listid[index]:
        luckyid = listid[i] 
print(f"Winner: {luckyid}")
    '''
'''
lucky = int(input("Enter lucky number : "))
candidate = int(input("Enter amount of candidates : "))
listid = []
countlucky = []
for i in range(candidate):
    id = input(f"Enter ID card number {i+1}: ")
    listid.append(int(id))
    countlucky.append(id.count(str(lucky)))
maxcount = max(countlucky)
luckyid = listid[countlucky.index(maxcount)]
for i in range(candidate):
    if countlucky[i] == maxcount and listid[i]>luckyid:
        luckyid = listid[i]
print(f"Winner: {luckyid}")'''

#11
'''
n = int(input("N: "))
m = int(input("M: "))
listnum = []
newlist = []
for i in range(n):
    x = int(input(f"Input number {i+1}: "))
    listnum.append(x%m)

#listnum = [1,2,0,2]
for i in listnum:
    if i not in newlist:
        newlist.append(i)
print(len(newlist))
'''
#12
'''
from typing import List
def commaCode(myList):
    result = ""
    
    for i in range(len(myList)):
        if len(myList)==1:
            return myList[0]
        elif i == len(myList)-1:
            result += f"and {myList[i]}"
        else:
            result += f"{myList[i]}, "
    return result
input_list = input("Input: ").split()
print(commaCode(input_list))
'''

#13
'''
#n = int(input("number :")):
def up(n):
    count = 1
    for x in range(n):
        print(" "*(n-x-1),end = '')
        print("+"*(count))
        count+=2
def down(n):
    count = n+4
    for i in range(n):
        print(" "*i,end = '')
        print("+"*(count))
        count-=2
def right(n):
    for i in range(1,n+1):
        for j in range(i):
            print("+",end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("+",end='')
        print()
def left(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end = '')
        
        print("+"*(i),end = '')
        print()
    for i in range(1,n):
        for j in range(i):
            print(" ",end = '')
        
        print("+"*(n-i),end = '')
        print()
n = int(input("Enter arrow's size (n): "))
d = input("Enter direction (u d l r): ")
if d=='u':
    up(n)
elif d=='d':
    down(n)
elif d=='l':
    left(n)
elif d=='r':
    right(n)
'''
