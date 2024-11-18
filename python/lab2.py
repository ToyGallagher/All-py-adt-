'''def distance(acceleration,time):
    v0 = 0
    s = (v0*time)+(1/2)*(acceleration*(time**2))
    return s'''
'''
import math
def circle(r):
    area = (math.pi)*(r**2)
    return area
def circumference(r):
    cir = 2*(math.pi)*r
    return cir
def sphere(r):
    sp = (4/3)*(math.pi)*(r**3)
    return sp
r = float(input("Enter a radius: "))
print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))
'''
'''
def sum_digits(n):
    num = list(str(n))
    x=0
    for i in num:
        i=int(i)
        x+=i
    print( x)
        
def digit(n):
    num = list(str(n))
    
    print( num[-1])

def tens(n):
    num = list(str(n))
    
    print( num[-2])

def hundreds(n):
    num = list(str(n))
    
    print( num[-3])
    
def thousands(n):
    num = list(str(n))
    
    print( num[-4])

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))
'''
'''
def sum_digits(n):
    return digit(n)+tens(n)+hundreds(n)+thousands(n)

def digit(n):
    return (((n%1000)%100)%10)
def tens(n):
    return (((n%1000)%100)//10)
def hundreds(n):
    return ((n%1000)//100)
def thousands(n):
    return n//1000
    
    

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))
'''
'''
def read_hour():
    h = int(input("Enter hour: "))
    return h 
def read_minute():
    m = int(input("Enter minute: "))
    return m 
def read_second():
    s = int(input("Enter second: "))
    return s
def to_seconds(h, m, s):
    total = h*3600+m*60+s
    return total

def time_elapsed(start_time,finish_time):
    result = finish_time-start_time
    h = result//3600
    m = (result-(h*3600))//60
    s = result-(h*3600)-(m*60)

    
    return f'{h} hours {m} minutes {s} seconds.'

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    #return hour,minute,second
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()

print('Elapsed time is', time_elapsed(start_time, finish_time))
'''
'''
def travel_speed(w):
   
    return 90/(30+w)+5

from math import ceil

def travel_time(s, d):
    hours = d/s
    day = ceil(hours/24)
    return day

def cal_sub_profit(distance, net_weight, sell_weight, cargo_price_per_ton, supply_price_per_day):
    speed = travel_speed(net_weight)
    cargo_price = sell_weight*cargo_price_per_ton
    supply_price = travel_time(speed,distance)*supply_price_per_day
    return cargo_price - supply_price

def calculate_profit():
    w_net = weight_a+weight_b+weight_c
    profit = cal_sub_profit(distance_oa,w_net,weight_a,price_a,price_s)
    
    w_net = weight_b+weight_c
    profit = profit + cal_sub_profit(distance_ab,w_net,weight_b,price_b,price_s)
 
    w_net = weight_c
    profit = profit + cal_sub_profit(distance_bc,w_net,weight_c,price_c,price_s)
  
    w_net = weight_o
    profit = profit + cal_sub_profit(distance_co,w_net,weight_o,price_o,price_s)
    return profit
def read_input():
    global price_a, price_b, price_c, price_o, price_s
    global weight_a, weight_b, weight_c, weight_o
    global distance_oa, distance_ab, distance_bc, distance_co
    weight_a = float(input("weight of cargo to A: "))
    weight_b = float(input("weight of cargo to B: "))
    weight_c = float(input("weight of cargo to C: "))
    weight_o = float(input("weight of cargo to O: "))
    price_a = float(input("price of cargo to A: "))
    price_b = float(input("price of cargo to B: "))
    price_c = float(input("price of cargo to C: "))
    price_o = float(input("price of cargo to O: "))
    price_s = float(input("price of supply: "))
    distance_oa = float(input("distance O to A: "))
    distance_ab = float(input("distance A to B: "))
    distance_bc = float(input("distance B to C: "))
    distance_co = float(input("distance C to O: "))

read_input()
profit = calculate_profit()
print("result profit is %.3f"%profit)
    
'''
