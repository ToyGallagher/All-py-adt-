'''
#5
def get_input():
    data_dict = {}
    while True:
        name = input("Enter name: ")
        if name == 'Q':
            break
        age = float(input("Enter scores: "))
        data_dict[name] = age
        
    return data_dict

def cal(data_dict):
    sum = 0
    less_than_60_list = []
    for key,val in data_dict.items():
        print(f'{key} got {val:.2f}')
    for val in data_dict.values():        
        if val<60:
            less_than_60_list.append(val)
            sum+=val
            avg = sum/len(less_than_60_list)
            #print(f'Average scores of students who got below 60 = {avg:.2f}')
    if len(less_than_60_list)>0:
        print(f'Average scores of students who got below 60 = {avg:.2f}')
    else:
        print('No one got below 60.')


x = get_input()
print(x)
cal(x)
'''
'''
#6
text = input('Enter text: ')
text_dict = {}
for i in text:
    if i != ' ':
        count = text.count(i)
        text_dict[i] = count
print(text_dict)
for key,val in text_dict.items():
    print(f"There are {val} {key}'s")
'''
'''
#8
def cloth_size(width_list):
    size_dict = {'S': 0, 'M': 0, 'L': 0}
    for i in range(len(width_list)):
        if width_list[i] <= 36:
            size_dict['S'] +=1
        elif 36 < width_list[i] <= 44 :
            size_dict['M'] +=1
        elif width_list[i]>44 :
            size_dict['L'] +=1
    return size_dict
print(cloth_size([50, 44, 40, 48]))
'''
'''
#9
import string
def count_char(word):
    word_dict = {}
    word = word.lower()
    for i in word:
        #if i != ' ' and i!=',' and i!='.' and i!="'":
        if i  in list(string.ascii_lowercase):
            word_dict[i] = 0
    for i in word:    
        if i in word_dict:
            word_dict[i]+=1
    return word_dict
print(count_char('Hello, There'))
'''
'''
#10
def count_words(s):
    word = {}
    s = s.split(' ')
    for i in s:
        word[i] = 0
    for i in s:
        if i in word:
            word[i] +=1
    return word
print(count_words('spam spam spam bacon and spam'))
'''
'''
#11
bid_dict = {}
name_list,price_list = [],[]
while True:
    bid = input()
    if bid == 'end':
        break
    else:
        name,price = bid.split()
        name_list.append(name)
        price_list.append(int(price))
        bid_dict[name] = [int(price),0]
        

        for i in name_list:
            count = name_list.count(i)
            bid_dict[i][1] = count
        #print(bid_dict)
name_list = name_list[(len(name_list)-len(bid_dict)):]
#print(name_list)
for i in name_list:
    if bid_dict[i][1] == 1:
        print(f"{i} bid at the price of {bid_dict[i][0]:.1f} baht in {bid_dict[i][1]} time.")
    else:
        print(f"{i} bid at the price of {bid_dict[i][0]:.1f} baht in {bid_dict[i][1]} times.")
#print(f"The winner is {bid_dict[max(bid_dict.values())]}.")
max_list = []
for i in bid_dict:
    max_list.append(bid_dict[i][0])
#print(bid_dict)
#print(max_list)
#print(max(max_list))
#index = max_list.index(max(max_list))

#print(f"The winner is {bid_dict}")
print(f"The winner is {list(bid_dict.keys())[list(bid_dict.values()).index(max(bid_dict.values()))]}." )  
#print(bid_dict)
#print(name_list)
'''
'''
#13
chem_formula = input()

number_list = [str(x) for x in range(10)]
cap_list = [chr(x) for x in range(65,91)]
merge_list = number_list + cap_list
data_dict = {}

i = 0 
while i < len(chem_formula):
    temp_str = ""
    temp_number = ""
    if chem_formula[i] in cap_list:
        temp_str += chem_formula[i]
        i += 1
        if i < len(chem_formula):
            while chem_formula[i] not in merge_list:
                temp_str += chem_formula[i]
                i += 1
                if i >= len(chem_formula):
                    break
        #print(temp_str,end = '')
        
        if i < len(chem_formula):
            while chem_formula[i] in number_list:
                temp_number += chem_formula[i]
                i += 1
                if i >= len(chem_formula):
                    break
       
        if len(temp_number) == 0:
            temp_number = 1
        else:
            temp_number = int(temp_number)
        
        data_dict[temp_str] = temp_number
        #print(data_dict)


find_formula = input()
if find_formula not in data_dict:
    print(0)
else:
    print(data_dict.get(find_formula))
#print(data_dict)
'''
'''
#14
word={'arm':['n','แขน'],'hello':['v','สวัสดี'],'beautiful':['adj','สวย'],\
    'toilet':['n','ห้องน้ำ'],'kick':['v','เตะ'],'handsome':['adj','หล่อ']}
while True:
    nuk = input()
    if nuk == '0':
        break
    elif nuk not in word:
        print("Word not in dictionary.")
        continue
    else:
        while True:
            choice = int(input())
            if choice != 1 and choice != 2:
                print("Invalid option.")
                continue
            else:
                print(word[nuk][int(choice)-1])
                break
'''
'''
#15
text = input("Text: ")
sub = input("Substring: ")
if text.find(sub) != -1:
    text = text.replace(sub,f"[{sub}]")
    print(text)
else:
    print("Not found")
'''
'''
#16
def process():
    if text.find(substr) != -1:
        result_text = text.replace(substr,f"[{substr}]")
    else:
        result_text = ""
'''  
'''
#17
def get_rna() -> str:
    dna_line = input("DNA: ")
    rna_line = ""
    dna_to_rna = {'A':'U', 'C':'G', 'G':'C', 'T':'A'}
    for i in range(len(dna_line)):
        rna_line += dna_to_rna[dna_line[i]]
    return rna_line

def synthesis(rna_line:str) -> int:
    start_codon = ["AUG"]
    stop_codon = ["UAA","UGA","UAG"]
    amino_acid = 0
    
    i = 0
    cont = True
    while i<len(rna_line) :
        start = i
        end = start+3
        temp_rna = rna_line[start:end]
        if temp_rna in start_codon:
            while temp_rna not in stop_codon:
                start = end
                end = start+3
                temp_rna = rna_line[start:end]
                amino_acid+=1
            i = end
            break
        i+=1
    return amino_acid
            

rna_line = get_rna()
#print(rna_line)
amino_count = synthesis(rna_line)
print(f"{amino_count} Amino acid(s)")
'''


'''
def get_rna():
    dna = input("DNA: ")
    rna = ""
    dna_to_rna = {'A':'U','C':'G', 'G':'C', 'T':'A'}
    for i in range(len(dna)):
        rna += dna_to_rna[dna[i]]
    return rna
def process(rna):
    start = ['AUG']
    stop = ["UAA","UGA","UAG"]
    amino_acid = 0
    i = 0
    condition = True
    while i < len(rna) and condition:


rna = get_rna()
'''
'''
#18
import re
def select_menu():
    print('Select menu :
1. add flight data
2. flight data by code
3. show all flight data
4. flight booking
5. show people flight data
6. exit')
def process():
    flight_data = dict()
    flight_code_dict = {}
    while True:
        menu = int(input("menu : "))
        if menu == 6:
            print("EXIT!!!!!!!!!!!!!!!")
            break
        elif menu == 1:
            x = input("Add data : ").split()
            flight_data.update({x[0]:[x[1],x[3],int(x[4]),int(x[6])]})
            #x = re.split(' -> | / | ', x)
            #flight_data[x[0]] = x[1:]
            #flight_data[x[0]][2] = int(x[3])
            #flight_data[x[0]][3] = int(x[4])
        elif menu == 2:
            code = input("Enter code : ")
            print(f"{code} is from {flight_data[code][0]} to {flight_data[code][1]}, number of people booking is {flight_data[code][2]}/{flight_data[code][3]}")
        elif menu ==3:
            print("All flight data")
            for i in flight_data.keys():
                print(f"{i} is from {flight_data[i][0]} to {flight_data[i][1]}, number of people booking is {flight_data[i][2]}/{flight_data[i][3]}")
        elif menu == 4:
            name_code_dict = {}
            
            name = input("Enter your name : ")
            flight_code = input("Enter flight code : ")
            if flight_data[flight_code][2]<flight_data[flight_code][3]:
                
                #flight_code_list = flight_code_list.append(flight_code)
                flight_data[flight_code][2] += 1
                if name in flight_code_dict:
                    flight_code_dict[name] += [flight_code]
                elif name not in flight_code_dict:
                    flight_code_dict[name] = [flight_code]
                print("Success")
            else:
                print("The flight is full, Sorry")
            #print(flight_code_dict)
        elif menu == 5:
            new_name = input("Enter your name : ")
            print(f"{new_name} is booking flight code = ",end = '')
            for i in range(len(flight_code_dict[new_name])):
                if i != len(flight_code_dict[new_name])-1:
                    print(flight_code_dict[new_name][i],end = ' ')
                else:
                    print(flight_code_dict[new_name][i])

            
select_menu()
process()
'''
'''
#19 pich
n=int(input())
relation={}
for i in range(n):
    temp=input().split()
    if temp[2]=='mother' or temp[2]=='father':
        if temp[0] not in relation:
            relation[temp[0]]=[temp[4]]
        else:
            relation[temp[0]]+=[temp[4]]
print(relation)
check=input().split()

count=0
for i in relation:
    
    if check[1] in relation[i] and check[3] in relation[i]:
        print('Yes')
        break
    elif count==len(relation)-1:
        print('No')
    count+=1
'''
'''
#19
round = int(input())
family = []
for i in range(round):
    case = input()
    case = case.replace('is','')
    case = case.replace('of','')
    case = case.split()
    family.append(case[0])
    family.append(case[2])

question = input()
who = []
who.append(question[3])
who.append(question[9])
if type(case[1]) == str  :
    if who[0] and who[1] in family:
        print("Yes")
    else:
        print("No")
#print(case) ['A', 'mother', 'B']
#print(who) 
#print(family) 
'''
'''
#20
n = int(input())
print('.'*n)
x=4
for i in range((n//2)-1):
    print('.'+(' '*i)+'.'+(' '*(n-x))+'.'+(' '*i)+'.')
    x+=2
print('.'+(' '*((n//2)-1))+'.'+(' '*((n//2)-1))+'.')
x = 1
for i in range((n//2)-1,0,-1):
    print('.'+(' '*(i-1)+'.'+(' '*(x))+'.'+(' '*(i-1)+'.')))
    x+=2
print('.'*n)
'''
'''
import csv
filename = input("Filename : ")
with open(filename) as f:
    datas = csv.reader(f)
    data = [ i for i in datas]
    print(data)
'''
'''
import csv
maxx = -1
minn = 1e9

def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data
filename = input("Filename : ")
print(read_csv(filename))
'''
'''
a = 0
cnt = 0
while -10<=a<=10:
    cnt +=1
    if a%5 == 1:
        a = a*2
    elif a%3 ==2:
        a = a+5
    elif a%2 == 0:
        a = a-4
    a = a-1
    print(a)
print(cnt)
print(-5%3)'''
'''
res = 0
for i in range(2):
    for j in range(i+1):
        #print(i,j)
        y = (i+j)%3
        if i <j :
            i = y
        elif j<i:
            j = y
        res= (i*j)
        print(res)
'''
a = [1,2,3,4,5,6]
b = a
for i in range(len(b)):
    b[i] = b[i]-1
print(b)
print(a)