#3
'''
class Item:
    def __init__(self,id,type,price):
        self.id = id
        self.type = type
        self.price = price
    def __str__(self):
        return f' id : {self.id}, type : {self.type}, price : {self.price}'
        
    def getType(self):
        return self.type
    def getPrice(self):
        return self.price
def idExist(id,res):
    return id in res.keys()
def whatisId(id,res):
    return res[id].getType()
def whatisPrice(id,res):
    return res[id].getPrice()

def getInput():
    item_dict = {}
    total_item = int(input("How many products are there? : "))
    for i in range(total_item):
        temp_id,temp_type,temp_price = input().split()
        item_temp = Item(temp_id,temp_type,temp_price)
        item_dict[temp_id] = item_temp #item_dict[123] = class Item
    return item_dict

def mainLoop(res):
    CONT = True
    while CONT:
        id = input("Id : ")
        if not idExist(id, res):
            print("This id doesn't exist.")
        else:
            while True:
                q = int(input("Q : "))
                if q == 1:
                    print(whatisId(id, res))
                elif q == 2:
                    print(whatisPrice(id, res))
                elif q == 3:
                    break
                elif q == 0:
                    CONT =False
                    break
res = getInput()
mainLoop(res)
'''
#4
'''
class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2*self.l + 2*self.w
    def is_square(self):
        if self.l == self.w:
            return "This rectangle is square too."
        else:
            return"This rectangle is not square."
class Triangle:
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def area(self):
        s = (self.l1+self.l2+self.l3)/2
        return (s*(s-self.l1)*(s-self.l2)*(s-self.l3))**(1/2)
    def perimeter(self):
        return self.l1+self.l2+self.l3
    def is_right_triangle(self):
        condition = False
        if self.l1**2 == self.l2**2 + self.l3**2:
            condition = True 
        if self.l2**2 == self.l1**2 + self.l3**2:
            condition = True
        if self.l3**2 == self.l1**2 + self.l2**2:
            condition = True
        if condition:
            return "This triangle is right triangle too."
        else:
            return "This triangle is not right triangle."
class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self) -> float:
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r


l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.')  
'''

#5
'''
class MyMath:
    def __init__(self):
        #temp_mul = 2*3*4
        #temp_sum = 3
        def fac(n):
            numfac=1
            for i in range(n):
                numfac*=i+1
            return numfac
        res = 0
        for i in range(50):
            if i%2==0:    
                res+=fac(2*(i+1)-1)/fac(4+2*i)
            else:    
                res-=fac(2*(i+1)-1)/fac(4+2*i)
            self.pi=3+4*(res)
            
    def is_even(self,num):
        self.num = num
        if self.num%2==0:
            return True
        else:
            return False
    def fac(self,num):
        self.num = num
        fact = 1
        for i in range(1,(self.num)+1):
            fact = fact * i
        return fact
    def is_prime(self,num):
        if num > 1:
   
            for i in range(2,num):
                if (num % i) == 0:
                    return False
                    break
                else:
                    return True
        else:
            return False
    def divide_by(self,num,k):
        if self.num%k==0:
            return True
        else:
            return False
    def ten_to_bi(self,num):
        bi=''
        while True:
            if num>=2:
                bi+=str(num%2)
                num = num//2
            else:
                bi+=str(num)
                break
        return bi[::-1]
    def ten_to_oct(self,num):
        oct=''
        while True:
            if num>=8:
                oct+=str(num%8)
                num//=8
            else:
                oct+=str(num)
                break
        return oct[::-1]
    def ten_to_sixteen(self,num):
        sixteen=''
        s2=['A','B','C','D','E','F']
        while True:
            if num>=16:
                if num%16>=10:
                    sixteen+=s2[num%16-10]
                else:
                    sixteen+=str(num%16)
                num//=16
                if num%16==0:
                    break
            else:
                if num>=10:
                    sixteen+=s2[num%16-10]
                    break
                else :
                    sixteen+=str(num)
                    break
        return sixteen[::-1]
    def int_to_roman(self,num):
        m=["", "M", "MM", "MMM"]
        c=["", "C", "CC", "CCC", "CD", "D",
             "DC", "DCC", "DCCC", "CM"]
        x=["", "X", "XX", "XXX", "XL", "L",
             "LX", "LXX", "LXXX", "XC"]
        i=["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]
  
        thousands=m[num//1000]
        hundreds=c[(num%1000)//100]
        tens=x[(num%100)//10]
        ones=i[num%10]
  
        roman = (thousands+hundreds+tens+ones)
        return roman
    

my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')
'''
'''
# 7
class py_solution():
    def __init__(self,inp_list) -> None:
        self.list = inp_list

    def is_valid_parentheses(self):
        temp_list = []
        open_list = ['(','{','[']
        
        for i in range(len(self.list)):  # ([)]
            if len(temp_list) == 0:
                temp_list.append(self.list[i]) # (
            else:
                if self.list[i] in open_list:  
                    temp_list.append(self.list[i])  #([)]
                else:
                    if self.list[i] == ')' and temp_list[len(temp_list)-1] == '(':
                        temp_list.pop() 
                    elif self.list[i] == ']' and temp_list[len(temp_list)-1] == '[':
                        temp_list.pop()
                    elif self.list[i] == '}' and temp_list[len(temp_list)-1] == '{':
                        temp_list.pop()
                    else:
                        temp_list.append(p_list[i])
                    
        if len(temp_list) == 0:
            return True
        else:
            return False


p_list = input("input: ")
p_check = py_solution(p_list)
if p_check.is_valid_parentheses():
    print("valid parentheses")
else:
    print("invalid parentheses")
'''

plist = input("Input : ")
templist = []
openlist = ['(','[','{']
closelist = [")","]","}"]  
for i in plist:    # }()[]  ()[]{}
    if i in openlist:   
        templist.append(i) # ({   (
    elif i  in closelist:
        pos = closelist.index(i)  
        if (len(templist)>0) and openlist[pos]==templist[len(templist)-1]:
            templist.pop()
        else:
            templist.append(i)
         
if len(templist)==0:
    print("balance")
else:
    print("unbalance")


#6 class matrix ans
'''
from typing import List

class Matrix:
    def __init__(self,data:List) -> None:
        self.data = data

    def det(self) -> int:
        diag_down,diag_up = 0,0
        for i in range(3):
            diag_down += self.data[0][i%3]*self.data[1][(i+1)%3]*self.data[2][(i+2)%3]
            diag_up += self.data[2][i%3]*self.data[1][(i+1)%3]*self.data[0][(i+2)%3]
        return diag_down-diag_up
    
    def plus(self,other):
        result = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(self.data[i][j] + other.data[i][j])
            result.append(list(temp))
        return Matrix(result)

    def minus(self,other):
        result = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(self.data[i][j] - other.data[i][j])
            result.append(list(temp))
        return Matrix(result)

    def multiply(self,other):
        result = []
        for i in range(3):
            temp_list = []
            for j in range(3):
                temp_sum = 0
                for k in range(3):
                    temp_sum += self.data[i][k] * other.data[k][j]
                temp_list.append(temp_sum)
            result.append(temp_list)
        return Matrix(result)

    def show(self) -> None:
        for i in range(3):
            for j in range(3):
                print(f'{self.data[i][j]:^6}', end = ' ')
            print()

def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()
'''
'''
#8
import numpy as np
class Princess:
    def __init__(self,blood):
        self.blood = blood
        self.attack = 10
    def attacking(self,time):
        return self.attack + time * 2
    def attacked(self,damage):
        self.blood = self.blood-damage
        if self.blood < 0:
            self.blood = 0 
    def heal(self):
        self.blood+=20
    def show_blood(self):
        return self.blood
class Monster:
    def __init__(self,blood):
        self.blood = blood
        self.attack = np.random.RandomState(1)
    def attacking(self):
        return self.attack.randint(1,40)
    def attacked(self,damage):
        self.blood = self.blood-damage
        if self.blood < 0:
            self.blood = 0
    def show_blood(self):
        return self.blood 
def battle(startblood):
    princess = Princess(startblood)
    monster = Monster(startblood)
    attacktime = 0
    while True:
        command = input("Attack(a) or Heal(h): ")
        if command == "a":
            monster.attacked(princess.attacking(attacktime))
            attacktime+=1
            print(f"Monster's HP left {monster.show_blood()}")
        if command== "h":
            princess.heal()
            attacktime = 0
            print(f"Your HP left {princess.show_blood()}")
        if monster.show_blood()==0:
            print("You win.(^_^)")
            break
        princess.attacked(monster.attacking())
        print(f"Monster's turn : Your HP left {princess.show_blood()}")
        if princess.show_blood() == 0:
            print("You lose and die.(T_T)")
            break
blood = int(input("Blood Start: "))
battle(blood)
'''
'''
# 9 
import numpy as np
from math import floor
from typing import List, NewType, Tuple, Union
class Princess:
    def __init__(self,blood,speed,heal_power):
        self.blood = blood
        self.speed = speed
        self.heal_power = heal_power
        self.combo = 0

    def attacking(self,time):
        return 10 + (self.combo * 2)
    def attacked(self,damage):
        self.blood = self.blood-damage
        if self.blood < 0:
            self.blood = 0 
    def heal(self) -> None:
        self.blood = self.blood + 20*self.heal_power
    def show_blood(self):
        return self.blood
    def increase_combo(self):
        self.combo = self.combo + 1
    def reset_combo(self):
        self.combo = 0
    def show_blood(self):
        return self.blood
    def show_speed(self):
        return self.speed
class Monster:
    def __init__(self,blood,speed,number):
        self.blood = blood
        self.speed = speed
        self.number = number
        
    def attacking(self,damage):
        return damage
    def attacked(self,damage):
        self.blood = self.blood-damage
        if self.blood < 0:
            self.blood = 0
    def show_number(self):
        return self.number

    def show_blood(self):
        return self.blood

    def show_speed(self):
        return self.speed
def princess_turn(princess:Princess,monster:Monster) -> Tuple[Princess,Monster]:
    print("- Your Turn -")
    command = input("Attack(a) or Heal(h): ")
    if command == 'a':
        monster.attacked(princess.attacking())
        princess.increase_combo()
        print(f"Monster {monster.show_number()} HP left {monster.show_blood()}")
    elif command == 'h':
        princess.heal()
        princess.reset_combo()
        print(f"Your HP left {princess.show_blood()}")
    return princess,monster

def monster_turn(monster:Monster,princess:Princess,atk_damage:int) -> Tuple[Monster,Princess]:
    print(f"- Monster {monster.show_number()} Turn -")
    princess.attacked(monster.attacking(atk_damage))
    print(f"Your HP left {princess.show_blood()}")
    return monster,princess
'''
