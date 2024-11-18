'''
age = int(input("Enter your age : "))
if age <=12:
    print("You are Child.")
elif age <= 18 and age>=13:
    print("You are Adolescence.")
elif age>=19 and age<= 59:
    print("You are Adult.")
elif age>=60:
    print("You are Senior Adult.")
'''
'''
import math
x = float(input("Input decimal: "))
x = math.floor(x)
for i in range(x):
    print(x ,end = ' ')
'''
'''
x = float(input("Input decimal: "))
x = int(x//1)
print((str(x)+' ')*x)
'''
'''
num1 = int(input("x: "))
op = input("Operator: ")
num2 = int(input("y: "))
if op == "+":
    result = num1+num2
    print(result)
elif op == "-":
    result = num1-num2
    print(result)
elif op == "*":
    result = num1*num2
    print(result) 
elif op == "/":
    result = num1/num2
    print(f"{result:.2f}")
elif op == "%":
    result = num1%num2
    print(result)
else:
    print("Unknown Operator")
'''
'''
w = int(input("Weight: "))
h = int(input("Height: "))
h = h/100    
bmi = w/(h)**2
if bmi>=30:
    print(f"Your BMI is {bmi:.1f} You're in the obese range. ")
elif bmi>=25 and bmi<=30:
     print(f"Your BMI is {bmi:.1f} You're in the overweight range. ")
elif bmi>=18.6 and bmi<=25:
     print(f"Your BMI is {bmi:.1f} You're in the healthy weight range. ") 
elif bmi<=18.6:
     print(f"Your BMI is {bmi:.1f} You're in the underweight range.")
'''
'''
target = 72
x = int(input("Enter your guess (0 - 100): ")) 
if x<0 or x>100:
    print("Sorry, out of range, try again later.")
elif x!= target:
    print("Sorry, your guess is wrong, try again later.")
elif x == target:
    print("Congratulations, your guess is correct.")
 '''   
'''
import math
t = int(input("Enter parking time in minutes: "))

print(f"Parking fee is {25*math.ceil(t/60)} baht.")  
'''
'''
import math
def sphere_volume(r):
    result1 = (4/3)*(math.pi)*(r**3)
    return result1
def sphere_surface_area(r):
    result2 = 4*math.pi*(r**2)
    return result2

r = float(input("Enter sphere radius: "))
a = sphere_volume(r)
b= sphere_surface_area(r)
print(f"Sphere volume is {a:.2f}")
print(f"Sphere surface area is {b:.2f}  ")
'''
'''
import math
x = float(input("Enter x : "))
if x < 0 :
    result = math.sqrt((x**2)+1)
    print(f"f({x:.2f}) = {math.ceil(result)}")
elif x == 0 :
    result = 0
    print(f"f({x:.2f}) = {0}")
elif x>0 and x<=99 :
    result = 3*(x**2)-(1-x)**2
    print(f"f({x:.2f}) = {result:.0f}")
elif x>99 :
    result = 2*(x**3)-(x)/(math.sqrt(x+1))
    print(f"f({x:.2f}) = {math.ceil(result)}")
'''
'''
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'
x = input("Username: ")
y = input("Password: ")
if x == ADMIN_USERNAME and y == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")
'''
'''
price = float(input("Enter buying amount: "))
if price >= 1000 and price<3000:
    realprice = (price*(90))/100
    print(f"Amount due after discount is {realprice:.2f} baht.")
elif price >=3000:
    realprice = (price*(85))/100
    print(f"Amount due after discount is {realprice:.2f} baht.")
else:
    price
'''
'''
x = int(input("Enter initial amount in Baht: "))
y = int(input("Enter interest rate in percent: "))
z=[]
for i in range(1,21):
     x = (x*(100+y))/100 
     z.append(f"{x:.2f}")


print(f"Total amount after 1 year is {z[0]} Baht.")
print(f"Total amount after 5 years is {z[4]} Baht.")
print(f"Total amount after 10 years is {z[9]} Baht.")
print(f"Total amount after 20 years is {z[19]} Baht.")
'''
'''
a = int(input(""))
b = int(input(""))
c = int(input(""))
datalist = [a,b,c]
newlist = []
while datalist:
    minimum = datalist[0]
    for i in datalist:
        if i<minimum:
            minimum = i
    newlist.append(minimum)
    datalist.remove(minimum)
print(newlist[0],newlist[1],newlist[2])
'''
'''
x = int(input("Input number: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
'''
def compute_rectangle_area(first_side, second_side):
    return first_side*second_side
def compute_surface_area(width,length,height):
    return  2*((width*height)+(length*height)+(width*length))
def compute_volume(width,length,height):
    return width*length*height

width = float(input("Enter width: "))
length = float(input("Enter length: "))
height = float(input("Enter height: "))
print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(width,length,height):.3f}")
print(f"Volume = {compute_volume(width,length,height):.3f}\n")

width,length,height = width*2,length*2,height*2

print("After doubling each side,")
print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(width,length,height):.3f}")
print(f"Volume = {compute_volume(width,length,height):.3f}")
'''
'''
while True:
    num = int(input("Input number: "))
    if num%2==0:
        print("Please input odd number")
    else:
        for i in range(1,num+1):
            print("x"*i)
        for i in range(num-1,0,-1):
            print("x"*i)
        break        
'''
'''
import math
def check_unit (area):

    """Check plural (square meter or square meters)"""
    if area>1:
        return "square meters."
    else:
        return "square meter."

def cal_circle (radius):

    """Calculate and return area result)"""
    return math.pi*
    (radius**2)

def cal_triangle (base,height):

    """Calculate and return area result)"""
    return (1/2)*base*height

def cal_rectangle (width,height):

    """Calculate and return area result)"""
    return width*height

def print_result (type,area,meter):

    """Print the area result with correct unit(s)"""
    print(f'Area of this {type} is {area:.2f} {meter}')

menu = input("(T)riangle (R)ectangle (C)ircle : ")
if menu == 'T' or menu == 't':
    b = float(input("base = "))
    h = float(input("height = "))
    result = cal_triangle(b,h)
    unit = check_unit(result)

    print_result('triangle',result,unit)

elif menu == 'R' or menu == 'r':

    
    w = float(input("width = "))
    h = float(input("height = "))
    result = cal_rectangle(w,h)
    unit = check_unit(result)

    print_result("rectangle",result,unit)

elif menu == 'C' or menu == 'c':
    inpr = float(input("Radius = "))
    result = cal_circle(inpr)
    unit = check_unit(result)
    print_result("circle",result,unit)
else:

    print("Incorrect Input!")
    '''

'''
def calpriceadult(adult):
    adultfee = adult*500
    return adultfee
def calpricechild(child):
    childfee = child*250
    return childfee
def tuesday(adult,child):
    totalprice = calpriceadult(adult)+calpricechild(child)
    disprice = (totalprice*25)/100
    print(f"Tuesday discount 25% = ({calpriceadult(adult)} + {calpricechild(child)}) x 25% = {disprice:.2f}")
    return disprice
def wednesday(adult,child):
    if  calpricechild(child)<1000:
        totalprice = calpriceadult(adult)+calpricechild(child)
        disprice = (totalprice*50)/100
        print(f"Wednesday discount 50% = ({calpriceadult(adult)} + {calpricechild(child)}) x 50% = {disprice:.2f}")
        return disprice
    elif calpricechild(child)>=1000:
        totalprice = calpriceadult(adult)+calpricechild(child)
        newdiscount = (calpricechild(child)*20)/100
        disprice = (totalprice*50)/100
        print(f"Wednesday discount 50% = ({calpriceadult(adult)} + {calpricechild(child)}) x 50% = {disprice:.2f}")
        print(f"Wednesday children over 1000 discount 20% = {calpricechild(child)} x 20% = {newdiscount:.2f}")
        return disprice+newdiscount
    
adult = int(input("How many adults?: "))  
child = int(input("How many children?: ")) 
day = input("Day (su,mo,tu,we,th,fr,sa): ")
if day in ("su","mo","th","fr","sa"):
     print(f"{adult} adults = {adult}x500 = {calpriceadult(adult)}")
     print(f"{child} children = {child}x250 = {calpricechild(child)}")
     totalprice = calpriceadult(adult)+calpricechild(child)
     print(f"Total price is {totalprice:.2f} Baht.")
elif day=="tu":
        print(f"{adult} adults = {adult}x500 = {calpriceadult(adult)}")
        print(f"{child} children = {child}x250 = {calpricechild(child)}")
        totalprice = calpriceadult(adult)+calpricechild(child)-tuesday(adult, child)
        print(f"Total price is {totalprice:.2f} Baht.")
elif day == "we":
        print(f"{adult} adults = {adult}x500 = {calpriceadult(adult)}")
        print(f"{child} children = {child}x250 = {calpricechild(child)}")
        
        totalprice = calpriceadult(adult)+calpricechild(child)-wednesday(adult, child)
        print(f"Total price is {totalprice:.2f} Baht.")
else:
    print("Incorrect input!")
  
    '''
'''
string = input("Enter a string: ")
size = int(input("Enter arrow's size (greater than 0): "))
if size > 0:
    for i in range(size//2):
        print(" "*i,end = '')
        print(string)
    if size%2!=0:
        print(" "*(size//2),end = '')
        print(string)
    for i in range(size//2,0,-1):
        print(" "*(i-1),end = '')
        print(string)
else:
    print("Size must be greater than 0.")'''

def cal_shipping_rate(weight):
    if weight<=100:
        shiprate = 0
    elif weight>100 and weight<=200:
        shiprate = 500
        return shiprate
    elif weight>200 and weight<=400:
        shiprate = 700
        return shiprate
    elif weight>400 and weight<=600:
        shiprate = 1000
        return shiprate
    elif weight>600 and weight<=800:
        shiprate = 1500
        return shiprate
    elif weight>800:
        shiprate = 2200
        return shiprate
    return shiprate
    
def getinput():
    x1 = int(input("How many AKB48 - Jiwaru Days [Type A] [Regular Edition] [CD+DVD]?: "))
    x2 = int(input("How many SKE48 - Ikinari PUNCH LINE [CD+DVD / Regular Edition / Type A]?: "))   
    x3 = int(input("How many SKE48 - Kakumei no Oka [3CD+DVD / Type A]?: "))
    x4 = int(input("How many Tofu Pro-Wrestling Regular Edition Blu-ray Box?: "))
    return x1,x2,x3,x4
def calweight(x1,x2,x3,x4):
    x1 = x1*298
    x2 = x2*298
    x3 = x3*505
    x4 = x4*945
    weight = x1+x2+x3+x4
    return weight
def calorderprice(x1,x2,x3,x4):
    x1 = x1*1646
    x2 = x2*1646
    x3 = x3*4104
    x4 = x4*22680
    orderprice = x1+x2+x3+x4
    return orderprice
def yen_to_usd(jpy):
    usd=jpy/108.210
    return usd

def yen_to_baht(jpy):
    baht=jpy/3.49909
    return baht
x1,x2,x3,x4 = getinput()
weight = calweight(x1,x2,x3,x4)
shiprate = cal_shipping_rate(weight)
orderprice = calorderprice(x1,x2,x3,x4)
usd1 = yen_to_usd(shiprate)
baht1 = yen_to_baht(shiprate)
usd2 = yen_to_usd(orderprice)
baht2 = yen_to_baht(orderprice)
total = shiprate+orderprice
usd3 = yen_to_usd(total)
baht3 = yen_to_baht(total)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Order weight is {weight:.2f} g")
print(f"Shipping rate is {shiprate:.2f} yen ({usd1:.2f} USD) ({baht1:.2f} THB)")
print(f"Order price is {orderprice:.2f} yen ({usd2:.2f} USD) ({baht2:.2f} THB)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Total price is {total:.2f} yen ({usd3:.2f} USD) ({baht3:.2f} THB)")
print(f"Your payment is {total:.2f} yen ({usd3:.2f} USD) ({baht3:.2f} THB)")
