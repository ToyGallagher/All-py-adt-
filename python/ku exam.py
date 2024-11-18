'''
number = int(input("enter a number : "))
x=[]
while number>=0:
    number = int(input("enter a number : "))
    x.append(int(number))
print(x)
'''

x= []
y=[]
number = int(input("Enter a number: "))
while number >= 0:
    x.append(int(number))
    number = int(input("Enter a number: "))
x.sort()
print("The numbers are")
for i in x:
    print(i)
    if i%3 != 0:
        y.append(i)
print("Found",len(y),"numbers.")


''' ของพี่เจล
n = 0
num_list = []
num = int(input("Enter a number: "))
while num >= 0:
    num_list.append(int(num))
    num = int(input("Enter a number: "))
if num <= 0 and len(num_list) != 0:
    print("The numbers are")
    num_list.sort()
    for i in range(len(num_list)):
        print(num_list[i])
    for i in range(len(num_list)):
        if num_list[i] % 3 != 0:
            n = n+1
    print(f'Found {n} numbers.')

'''


   
