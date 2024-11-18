'''x1 = input("Is Bulotelli injured?(y/n) ")

if x1 == "y":
    print("Not available") 
elif x1 == "n":
    x2 = input("Is Bulotelli late for the training?(y/n) ")
    if  x2 == "y":
        x3 = input("Did Bulotelli perform well in training?(y/n) ")
        if x3 =="n":
            print("Not selected")
        elif x3 == "y":
            print("Substitute")
    elif x2 == "n":
        print("Starter")'''
        



'''
import math
def getinput():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    d = int(input("Input d: "))
    e = int(input("Input e: "))
    return a,b,c,d,e
def getmean(a,b,c,d,e):
    mean = (a+b+c+d+e)/5
    return mean
def getsd(a,b,c,d,e,mean):
    sd = math.sqrt((((a-mean)**2)+((b-mean)**2)+((c-mean)**2)+((d-mean)**2)+((e-mean)**2))/5)
    return sd


a,b,c,d,e = getinput()
mean = getmean(a, b, c, d, e)
sd = getsd(a, b, c, d, e, mean)
print(f"mean: {mean:.3f}")
print(f"sd: {sd:.3f}")'''


'''
time = int(input("Minutes before due: "))
temperature = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")
days = (time//60)//24
hours = (time//60)%24
if hours >= 12:
    days += 1
print(f">>> {days} days before due.")
if days<2:
    print(">>> I will do the assignment.")
elif days > 5:
    print(">>> I will not do the assignment.")
else:
    if temperature > 40 or (temperature > 25 and rain.lower() == 'y'):
        print(">>> I will not do the assignment.")
    else:
        print(">>> I will do the assignment.")
'''

'''
def getinput():
    x = int(input("Enter year: "))
    return x
def cal(x):
    if x<543:
        print("Invalid year.")
    elif x%4==0 and x%100!=0 or x%400==0:
        print(f"{x} is a leap year.")
    elif x%4==0 and x%100==0 or x%400!=0:
        print(f"{x} is not a leap year.")
    

x = getinput()
cal(x)'''

'''
x = int(input("How long have Buzz played ?: "))

h = x//60
m = (x%60)
price = 0
if m>20:
    h+=1
    price = 900*h
elif h ==0 and m>20:
    price == 900
else:
    price = 900*h

if h>=2 and h<4:
    price = (price*90)//100
elif h>=4 and h<5:   
    price = (price*80)//100 
elif h>=5:   
    price = (price*70)//100 
print(f"Total price is {price} baht.")
'''

'''
result_m = input("What's the result of Manchester city's match? ")
result_l = input("What's the result of Liverpool's match? ")  
if result_m == "won" and result_l == "lost":
    print("Manchester city is the champion of Premier League.")
elif result_l == "won" and result_m == "lost":
    print("Liverpool is the champion of Premier League.")
elif result_m == "won" and result_l == "won":
    margin_m = input("What is the margin that Manchester city won by? ")
    margin_l = input("What is the margin that Liverpool won by? ")
    if margin_m > margin_l:
        print("Manchester city is the champion of Premier League.")
    elif margin_l > margin_m:
        print("Liverpool is the champion of Premier League.")
    elif margin_m == margin_l:
        t = input("Which team won the play-off match?(Manchester city/Liverpool) ")
        if t == "Manchester city":
            print("Manchester city is the champion of Premier League.")
        elif t == "Liverpool":
            print("Liverpool is the champion of Premier League.")
'''
'''
tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))
price_tv = tv*6000
price_dvd = dvd*1500
price_audio = audio*3000
price_total = price_audio + price_dvd + price_tv
if price_total<24000:
    print(f"Total price is {price_total:.2f} baht.")
    print(f"Your payment is {price_total:.2f} baht. Thank you!")
elif price_total>=24000:
    price_discount = (price_total*20)/100
    price_result = price_total-price_discount
    print(f"Total price is {price_total:.2f} baht.")
    print(f"You've got a discount of {price_discount:.2f} baht.")
    print(f"Your payment is {price_result:.2f} baht. Thank you!")
'''
'''
def fibonacci(n):
    a = 0
    b = 1
     
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
x = int(input("Enter n: "))
result = fibonacci(x)
print(f"fibo({x}) = {result}")'''
'''
def fibo(n):
    listnum = [1,1]
    for i in range(2,n):
        listnum.append(listnum[i-1] + listnum[i-2])
    return listnum[-1]
print("fibo({n}) = {x}".format(n=n,x=fibo(n)))
'''

'''
def inputShape():
    x = int(input("Input Shape: "))
    return x

def calculateSphere():
    r = int(input("Input radius(meter): "))
    volume = (4/3)*pi*(r**3)
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume


def calculateCone():
    r = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    volume = (1/3)*pi*(r**2)*h
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculateCylinder():
    r = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    volume = pi*(r**2)*h
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculatePrism():
    x = int(input("Input width(meter): "))
    y = int(input("Input length(meter): "))
    z = int(input("Input height(meter): "))
    volume = x*y*z
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculatePyramid():
    x = int(input("Input width(meter): "))
    y = int(input("Input length(meter): "))
    z = int(input("Input height(meter): "))
    volume = (x*y*z)/3
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculatePrice(v):
    price = int(input("Price(Bath) per 1 cubic meter: "))
    pricetotal = v*price
    print(f"The price is {pricetotal:.2f} Baht.")
pi = 3.141592653589793
x = inputShape()
if x == 1:
    volume = calculateSphere()
        
elif x == 2:
    volume = calculateCone()
        
elif x ==3:
    volume = calculateCylinder()
        
elif x ==4:
    volume = calculatePrism()
        
elif x ==5:
    volume = calculatePyramid()
        

calculatePrice(volume)
'''

'''
def burger():
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    sub = input("Enter your choice: ").upper()
    if sub == 'R':
        name = "Regular Burger"
        price = 60
    elif sub == 'C':
        name = "Cheese Burger"
        price = 75
    elif sub == 'D':
        name = "Double Cheese Burger"
        price = 90
    else:
        print("Invalid sub menu choice.")
        return
    print(f"Your {name} is {price} Baht.")

def chicken():
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    sub = input("Enter your choice: ").upper()
    if sub == 'F':
        name = "Fried Chicken"
        price = 120
    elif sub == 'G':
        name = "Grilled Chicken"
        price = 150
    elif sub == 'C':
        name = "Chef's Chicken"
        price = 180
    else:
        print("Invalid sub menu choice.")
        return
    print(f"Your {name} is {price} Baht.")

def pasta():
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    sub = input("Enter your choice: ").upper()
    if sub == 'S':
        name = "Spaghetti de Italiano"
        price = 90
    elif sub == 'L':
        name = "Lasagna Supreme"
        price = 120
    elif sub == 'M':
        name = "Macaroni Special"
        price = 100
    else:
        print("Invalid sub menu choice.")
        return
    print(f"Your {name} is {price} Baht.")

print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
meal_type = input("Enter your choice: ").upper()
if meal_type == 'B':
    burger()
elif meal_type == 'C':
    chicken()
elif meal_type == 'P':
    pasta()
else:
    print("Invalid main menu choice.")'''
'''
if a >= b and a >= c and a >= d:
    four = a
    if b >= c and b >= d:
        three = b
        if c >= d:
            two = c
            one = d
        else:
            two = d
            one = c
    if c >= b and c >= d:
        three = c
        if b >= d:
            two = b
            one = d
        else:
            two = d
            one = b
    if d >= b and d >= c:
        three = d
        if b >= c:
            two = b
            one = c
        else:
            two = c
            one = b

if b >= a and b >= c and b >= d:
    four = b
    if a >= c and a >= d:
        three = a
        if c >= d:
            two = c
            one = d
        else:
            two = d
            one = c
    if c >= a and c >= d:
        three = c
        if a >= d:
            two = a
            one = d
        else:
            two = d
            one = a
    if d >= a and d >= c:
        three = d
        if a >= c:
            two = a
            one = c
        else:
            two = c
            one = a

if c >= a and c >= b and c >= d:
    four = c
    if a >= b and a >= d:
        three = a
        if b >= d:
            two = b
            one = d
        else:
            two = d
            one = b
    if b >= a and b >= d:
        three = b
        if a >= d:
            two = a
            one = d
        else:
            two = d
            one = a
    if d >= b and d >= a:
        three = d
        if b >= a:
            two = b
            one = a
        else:
            two = a
            one = b

if d >= a and d >= b and d >= c:
    four = d
    if a >= b and a >= c:
        three = a
        if b >= c:
            two = b
            one = c
        else:
            two = c
            one = b
    if b >= a and b >= c:
        three = b
        if a >= c:
            two = a
            one = c
        else:
            two = c
            one = a
    if c >= a and c >= b:
        three = c
        if a >= b:
            two = a
            one = b
        else:
            two = b
            one = a
'''
'''
def check_prime(num):
    if num >=1:
        for i in range(2,num):
            if (num % i) == 0:
               return False
        return True   
    else:
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")
'''

'''
def fac(n,r):
    result = 1
    for x in range(n-r+1,n+1):
        result = x*result
    return result
print(fac(7, 3))
'''
