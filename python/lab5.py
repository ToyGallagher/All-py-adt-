#1
'''
def getinput():
    num=[]
    while True:
        n=input('Enter a number (to quit, just [Enter]): ')
        if n=='':
            break
        else:
            n=float(n)
            num.append(n)
            continue
    return num
def checklen(num):
    if len(num)==0:
        print("Nothing to do.")
        exit()
def minmax(num):
    print(f"Maximum value is {max(num):.2f}")
    print(f"Minimum value is {min(num):.2f}")
    return num
def cal_average(num):
    x = 0
    for i in num:
        x+=i
    average = x/len(num)
    print(f"Average value is {average:.2f}")
    return average
n = getinput()
checklen(n)
x = minmax(n)
cal_average(x)
'''

#2 sum of number
'''
sum1 = 0
sum2 = 0
while True:
    
    x = float(input("Enter a number (or 0 to exit): "))
    if x>0:
        sum1 += x
        continue
    elif x<0:
        sum2 += x
        continue
    elif x==0:
        break
print(f"Sum of positive numbers is {sum1:.2f}")
print(f"Sum of negative numbers is {sum2:.2f}")   
'''
#3 score statistics
'''
total = 0
average = 0
count = 0
score = []

while True:
    x = input("Input score (or just ENTER to finish): ")
    if x =='':
        break
    else:
        count+=1
        number = x
        total += int(number)
        score.append(int(x))
        average = total/count
    
for i in range(len(score)):
    print(f"Score #{i+1}: {score[i]}")
print(f"Average score is {average:.2f}")
print(f"Minimum score is {min(score)}")
print(f"Maximum score is {max(score)}")
'''
#4
'''
def getinput():
    num = []
    while True:
        n = input("Input score (or just ENTER to finish): ")
        if n =='':
            break
        else:
            n = float(n)
            num.append(n)
    return num

def calaverage(num):
    sum = 0
    for i in num:
        sum+=i
    average = sum/len(num)
    print(f"Average score is {average:.2f}")
    return average
def calsd(num,average):
    sqsum = 0
    for i in num:
        sqsum += (i-average)**2
    sd = (sqsum/(len(num)-1))**0.5
    print(f"Standard deviation is {sd:.2f}")
    return sd

def calgrade(num,average,sd):
    for i in range(len(num)):
        if num[i] >= avg+1.5*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: A")
        elif num[i] >=avg+sd and num[i]< avg+1.5*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: B+")
        elif num[i] >=avg+0.5*sd and num[i]< avg+1.0*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: B")
        elif num[i] >=avg and num[i]< avg+0.5*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: C+")
        elif num[i] >=avg-0.5*sd and num[i]< avg:
            print(f"Score #{i+1}: {num[i]:.0f} grade: C")
        elif num[i] >=avg-sd and num[i]< avg-0.5*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: D+")
        elif num[i] >=avg-1.5*sd and num[i]< avg-sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: D")
        elif num[i] < avg-1.5*sd:
            print(f"Score #{i+1}: {num[i]:.0f} grade: F")
   
x=getinput()
avg = calaverage(x)
sd = calsd(x, avg)
calgrade(x, avg, sd)
'''

#5
'''
def getinput():
    score = []
    while True:
        x = input("Input score (or just ENTER to finish): ")
        if x=='':
            break
        else:
            x=int(x)
            score.append(x)
            continue
    return score
def calrank(score):
    #while score:
        #maximum = score[0]
        #for i in score:
            #if i > maximum:
                #maximum = i
        #new.append(maximum)
        #score.remove(maximum)
    #print(new)
    for i in range(len(score)):
        for j in range(i+1,len(score)):
             if score[i]<score[j]:
                score[i],score[j] = score[j],score[i]
    return score    
def showranking(score):
    for i in range (0,len(score)):
        print(f"Rank #{i+1}: {score[i]}")
n = getinput()
x = calrank(n)
showranking(x)
'''
#6
'''
password = "I love programming"
for i in range(1,4):
    x = input("Enter the password: ")
    if x != password:
        print(f"Incorrect password, attempt #{i}")
        print("Access not allowed")
        if i == 3:
            print("Maximum attempts exceeded")
    elif x == password:
        print("Correct password")
        print("Access granted")
        exit()
'''

# 7
'''
x = input("Input a string: ")
y=[]
for i in x:
    y.append(i)
#y = ['h', 'e', 'l', 'l', 'o']
print(y[0])
for i in range(1,len(x)):
    print(" "*(i-1),y[i])
'''
'''
x = input("Input string : ")
for i in range(len(x)):
    for j in range(i):
        
        print(" ",end = '')
    print(x)'''
#8
'''
depth_of_well = int(input("Enter the depth of the well: "))
jump_high = int(input("How high the frog can jump up? "))
slips_high = int(input("How far the frog slips down? "))
days = 0
if depth_of_well == jump_high:
    print("The frog can escape the well on day 1.")
elif jump_high == slips_high:
    print("The frog will never escape from the well.")
else:
    while True:
        depth_of_well -= jump_high 
        days += 1
        if depth_of_well>0:
            print(f'On day {days} the frog leaps to the depth of {depth_of_well} meters.')
            print(f'At night he slips down to the depth of {slips_high+depth_of_well} meters.') 
            depth_of_well+=slips_high
        else:
            print(f"The frog can escape the well on day {days}.")
            break
'''

#9
'''
def getinput():
    n=int(input('How many food you have : '))
    return n

def plus(total,value):
    return total+value

def minus(total,value):
    return total-value

n=getinput()
last_total=0

for i in range(n):
    total,value=map(int,input().split())
    if value==-1:
        last_total+=minus(0,total)
    elif value==1:
        last_total+=plus(0,total)

print(last_total)
'''
#10
'''
def getinput():
    d=int(input('Distance from starting point(m.): '))
    return d

def style1(x):
    move1 = x+5
    move2 = move1-2
    return move1,move2

def style2(x):
    move1=x-4
    move2=move1+3
    return move1,move2

move1 = 0
move2 = 0
moveset = 0
d = getinput()
while move2 != d:
    if d == 0:
        break
    elif move2<d:
        move1,move2 = style1(move2)
        print(move1,move2,end = ' ')
        moveset+=1
    elif move2>d:
        move1,move2=style2(move2)
        print(move1,move2,end=' ')
        moveset+=1
if d!=0:
    print()
    print(f'Buzz moved {moveset} set(s)')
elif d==0:
    print("0")
    print("Buzz moved 0 set(s)")
'''
#11
'''
def fibo(n):
    listnum = [1,1]
    for i in range(2,n):
       listnum.append(listnum[i-1] + listnum[i-2])
    return listnum[-1]

#print("fibo({n}) = {x}".format (n=n,x=fibo(n)))

n = int(input("Day: "))     
for i in range(1,n+1):
    print(fibo(i),end = ' ')'''
#12
'''
time = int(input("Estimated time : "))
ntime = time*2.5
week = time//8
x,y,z = 0,0,0
for i in range(week):
    print(f"Week{i+1}")
    x1 = int(input("Physical therapy : "))
    y1 = int(input("Weight training : "))
    z1 = int(input("Fitness training : "))
    x+=x1
    y+=y1
    z+=z1
if x<ntime or y<ntime or z< ntime:
    print('Buzzy has not recovered in time.')
else:
    print('Buzzy has recovered in time.')
#if x==ntime and y == ntime and z == ntime:
    #print("Buzzy has recovered in time.")
#elif x<ntime or y < ntime or z < ntime:
    #print("Buzzy has not recovered in time.")
'''
#13 
'''
n = 0
d = 0
d0 = 100
while d<d0:
    x = int(input("Input distance: "))
    d += x
    n+=1
    d0 += 2**n
    print(f"Police distance: {d}")
    print(f"Criminal distance: {d0}")
else:
    print("Caught him!")
'''
#14 
'''
x = int(input())
y = int(input())
p = int(input())
line = 0
while x <= y:
    if x%p != 0:
        print(x,end = ' ')
        x+=1
    else:
        x += 11
        continue
    line+=1
    if line%10 == 0:
        print()

    #if line == 10:
        #line = 1
        #print()
    #else:
        #line += 1
'''

#15
'''
from collections import Counter
num = []
while True:
    x = int(input())
    if x==0:
        break
    else:
        num.append(x)
        

    #num = [2,5,5,5,5,3]

for i in range(len(num)-1):
    num2 = []
    if num[i] == num[i+1] :
        num2.append(num[i])
        continue
    print(num2)'''

#16
'''
def altrnating_sum(n):
    p=[]
    m=[]
    for i in range(1,n+1):
        if i%2==0:
            x = -i
            m.append(x)
        else:
            p.append(i)
    return sum(p)+sum(m)
    
n = int(input("Enter n of series: "))
altrnating_sum(n)
print("Alternating Sum from 1 to {:d} is {:d}".format(n,altrnating_sum(n)))
'''
#17
'''
def find_last_product(a:int,b:int,c:int) -> str:
    count_zero = 0
    while count_zero < 2:
        if a >= c and b >= c:
            a,b = a-1,b-1
            if a == 0:
                count_zero += 1
            if b == 0:
                count_zero += 1
            if c == 0:
                count_zero -= 1
            c = c+1
        elif a >= b and c >= b:
            a,c = a-1,c-1
            if a == 0:
                count_zero += 1
            if c == 0:
                count_zero += 1
            if b == 0:
                count_zero -= 1
            b = b+1
        elif b >= a and c >= a:
            b,c = b-1,c-1
            if b == 0:
                count_zero += 1
            if c == 0:
                count_zero += 1
            if a == 0:
                count_zero -= 1
            a = a+1
    if a == 1:
        return 'A'
    elif b == 1:
        return 'B'
    else:
        return 'C'

total_a = int(input("A: "))
total_b = int(input("B: "))
total_c = int(input("C: "))
print(find_last_product(total_a,total_b,total_c))'''
'''
def find_last_product(a,b,c):
    while ( a!=0 and   b!=0) or  ( b!=0 and  c!= 0) or (a!=0 and  c!=0):
        if a>=b>=c:
            a-=1
            b-=1
            c+=1
        elif b>=a>=c :
            a-=1
            b-=1
            c+=1
        elif b>=c>=a:
            a+=1
            b-=1
            c-=1
        elif c>=b>=a:
            a+=1
            b-=1
            c-=1
        elif a>=c>=b:
            a-=1
            b+=1
            c-=1
        elif c>=a>=b:
            a-=1
            b+=1
            c-=1
    if b==0 and c ==0:
        return 'A'
    elif a==0 and c==0:
        return 'B'
    elif a==0 and b==0:
        return 'C'
total_a = int(input("A: "))
total_b = int(input("B: "))
total_c = int(input("C: "))
print(find_last_product(total_a,total_b,total_c)) '''
#18
'''
def count_digits(number):
    number = str(number)
    i = 0
    count = 0
    while i<len(number):
        if number[i].isdigit():
            count+=1  
        i+=1
    return count
# Main
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")
'''
#18.5 
'''
while True:
    number = input("Enter number (E for exit): ")
    if number.upper()=="E":
        print("Bye")
        break
    else:
        number = int(number)
        print(f"There are {count_digits(number)} digits in {number}")
'''
#19
'''
def count_digits(number):
    number = str(number)
    return len(number)

def get_last_digit(n):
    """
    Get last digit in number
    :params number is an integer
    :return last digit in number

    >>> get_last_digit(41)
    1
    >>> get_last_digit(394)
    4
    >>> get_last_digit(1020)
    0
    """
    number = str(n)
    last_digit = number[len(number)-1]
    return last_digit
   
def get_distribution(number):
    """
    Return string showing distribution of number
    :params number (int): a number to find distribution
    :return string
    >>> get_distribution(21)
    '1x10^0 + 2x10^1'
    >>> get_distribution(306)
    '6x10^0 + 0x10^1 + 3x10^2'
    >>> get_distribution(12201)
    '1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4'
    """
    result = ""
    digits = count_digits(number)
    for i in range(0,digits):
        temp = get_last_digit(number)
        number = number//10
        if i < digits-1:
            result += f"{temp}x10^{i}" + ' + '
        else:
            result += f"{temp}x10^{i}"
    return result
   
# Main
while True:
    inp_number = int(input("Input number (negative number to quit): "))
    if inp_number>=0:
        distribute_number = get_distribution(inp_number)
        print(f"{inp_number} = {distribute_number}")
    else:
        break
'''
#20
'''
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

x = int(input("Input k: "))
#if x == 0:
    #print("0! = 1")
    #print("Summation of factorial 1!-0! = 1")
#else:
fac = 0
for i in range(1,x+1):
    print(f"{i}! = {factorial(i)}")
    fac += factorial(i)
print(f"Summation of factorial 1!-{x}! = {fac}")
'''
'''
from collections import Counter
data_list = [7,8,5,9,8,5,9,5,9,9]
new_list = []
m = {}
while data_list:
    maximum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x > maximum:
            maximum = x
    new_list.append(maximum)
    data_list.remove(maximum)    

#print (new_list) 
for i in new_list:
    if i in m:
        m[i]+=1
    else:
        m[i]=1    
'''
'''
x = "hello"
for i in range(len(x)): #5
    for j in range(i):
        print(" ",end = '')
    print(x[i])
'''

  

'''
n, s = [int(i) for i in input().strip().split()]
#print(n, s)

std = []
i = 0
while i < n:
  tmp = [i for i in input().strip().split()]
  if len(tmp) != s + 1: 
    print('Error: input, re-enter this student info!')
    print('hint: must be name followed by subjects\'s scores')
    continue
  t = []
  t.append(tmp[0])
  t.append([int(tmp[j]) for j in range(1, s+1)])
  std.append(t)
  print(std)
  i += 1'''
'''
for x in range(1,6):
  for y in range(6 - x):
    print (" ",end="")
  for y in range(1,x + 1):
    print(y,end="")
  for y in range(2,x + 1):
    print(x - y + 1,end="")
  print()
for x in range(4,0,-1):
  for y in range(6 - x):
    print (" ",end="")
  for y in range(1,x + 1):
    print(y,end="")
  for y in range(2,x + 1):
    print(x - y + 1,end="")  
  print()'''
'''
n = 5
for x in range(1,n+1):
   for y in range(n - x):
    print (" ",end="")
   for y in range(1,x + 1):
    print("+",end="")
   print()
for x in range(4,0,-1):
   for y in range(n - x):
    print (" ",end="")
   for y in range(1,x + 1):
    print("+",end="")
   print()'''