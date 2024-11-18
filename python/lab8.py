#1
'''
def getInput():
    lloan,lcompound,lmonth=[],[],[]
    i=0
    while True:
        loan=int(input('Loan : '))
        if loan==-1 and i==0:
            print('It\'s bad day.')
            break
        elif loan==-1:
            break
        else:
            lloan.append(loan)
        lcompound.append(int(input('Compound interest : ')))
        lmonth.append(int(input('Month : ')))
        
        i+=1
    return lloan,lcompound,lmonth

def calTotal(loan,compound,month):
    ltotal=[]
    for i in range(len(loan)):
        for j in range(1):
            total=loan[i]*((compound[i]/12+100)/100)**month[i]
        ltotal.append(total)
    return ltotal

def showData(ltotal):
    dayTotal=sum(ltotal)
    for i in range(len(ltotal)):
        print(f'Customer number : {i+1}\nTotal : {ltotal[i]:.2f}')
    print(f'Today Total : {dayTotal:.2f}')


loan,lcompound,lmonth=getInput()
if len(loan)>0:
    ltotal=calTotal(loan,lcompound,lmonth)
    showData(ltotal)
else:
    pass
'''
#2
'''
callcode = input("Encode or Decode : ")
number = [1,2,3,4,5,6,7,8,9,0]*90
if callcode=='E' or callcode=='D':
    
    source = input('Source : ')
   
    shifter = int(input('Shifter : '))
    print('Destination : ',end='')
    if callcode=='E':
        for i in source:
            i=int(i)
            index=number.index(i)
            print(number[index+shifter],end='')
    elif callcode=='D':
        for i in source:
            i=int(i)
            index=number.index(i)
            print(number[index-shifter],end='')         
else:
    print('Call Army!!!')
'''
'''
number = [1,2,3,4,5,6,7,8,9,0]
source = "12345"
for i in source:
    i = int(i)
    print(number.index(i))'''
#3
'''
num = int(input("Order of Tribonacci(n): "))
tri = [1,1,1]
for i in range(3,num):
    tri.append(tri[i-1]+tri[i-2]+tri[i-3])
print("Serie(s): ",end = '')
for i in tri:
    print(i,end =' ')
'''
#4
'''
n = int(input("n = "))
num = []
while len(num)!=(n-1):
    for i in range(1,n):
        num.append(i)
#num = 1,2,3,4
result = 1
resultlist = [1]
for i in range(len(num)):
    result += num[i]
    resultlist.append(result)

print("Serie(s): ",end = '')
for x in resultlist:
    
    print(x,end=' ')
'''
#อีกวิธี
'''
ntotal,i=1,0
n=int(input('n = '))
print('Serie(s): ',end='')
while i<n:
    ntotal+=i
    print(ntotal,end=' ')
    i+=1
'''
#5
'''
w = input("Woody's Cards: ").split()
b = input("Buzz's Cards: ").split()
point=list('AKQJT98765432')
card = ['S','H','D','C']
wscore = 0
bscore = 0
for i in range(5):
    if point.index(w[i][0])<point.index(b[i][0]):
        wscore+=1
    elif point.index(w[i][0])>point.index(b[i][0]):
        bscore+=1
    else:
        if card.index(w[i][1])<card.index(w[i][1]):
            wscore+=1
        else:
            bscore+=1
if wscore>bscore:
    print('Winner is Woody !!')
else:
    print("Winner is Buzz !!")
'''

#6
'''
word = input("Truth word is ")
list,newlist = [],[]
while True:
    x = input()
    if x == "-1":
        break
    else:
        list.append(x)
        continue
for i in list:
    if i in word:
        newlist.append(i)
if list == newlist:
    print("Truth!")
else:
    print(f"Lie! and hit = {len(newlist)}")
'''

#12
'''
def split_str(s,delim=' '):
    ls=[]
    while True:
        if s.find(delim)==-1:
            ls.append(s)
            break
        index=s.index(delim)
        ls.append(s[:index])
        s=s[index+1:]
    return ls'''
'''
def split_str(s,delim=' '):
    x = []
    split = ""
    for i in range(len(s)):
        if s[i]==delim:
            x.append(split)
            split = ""
        else:
            split+=s[i]
            if i == len(s)-1:
                if s[i]!=delim:
                    x.append(split)
    return x
print(split_str('apple', '|'))'''
#13
'''
def print_vmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[len(a)-1-i][j]}",end=' ')
        print()
def print_hmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][len(a)-1-j]}",end=' ')
        print()
def get_input(n):
    matrix_list = []
    for i in range(n):
        temp_list = [x for x in input().split()]
        matrix_list.append(temp_list)
    return matrix_list


direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))
matrix_list = get_input(size)
print("After flip:")
if direction == 'V':
    print_vmatrix(matrix_list)
else:
    print_hmatrix(matrix_list)
'''
#14
'''
def print_table(row,col):
    maxrc = 8
    for i in range(maxrc):
        print('-----------------')
        if i == row:
            for j in range(maxrc):
                if j == col:
                    print("|R",end = '')
                else:
                    print("|x",end = '')
            print("| ")
        else:
            for j in range(maxrc):
                if j == col:
                    print("|x",end = '')
                else:
                    print("| ",end = '')
            print("| ")
    print('-----------------')
'''
rook_row = int(input("Enter Rook's row position: "))
rook_col = int(input("Enter Rook's column position: "))
print_table(rook_row,rook_col)

'''
#15
n = int(input("Enter the number of rows or columns : "))
for i in range(0,n):
    for j in range(1+i,n+i+1):
        print('%2d' % j,end = ' ')
    print()
'''