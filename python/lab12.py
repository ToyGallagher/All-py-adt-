#2
'''
file_name = input("Enter score file: ")
file_data = open(file_name).read().splitlines()
file_data = [int(i) for i in file_data if i != ""]
for i in range(len(file_data)):
    print(f"Student #{i+1} score: {file_data[i]}")
print(f"Average score is {(sum(file_data)/len(file_data)):.2f}")
print(f"Minimum score is {min(file_data)}")
print(f"Maximum score is {max(file_data)}")
'''
'''
#3
def read_table(filename):
    file_data = open(file_name).read().splitlines()
    new_file_data = [x.split(",") for x in file_data if x != ""]
    for row in new_file_data:
        row[1] = int(row[1])
        row.append(grade_point(row[2]))
    return new_file_data

def grade_point(grade):
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    elif grade == "F":
        return 0.0
def print_table(table):
    for row in table:
        print(f"subject: {row[0]} credits: {row[1]} grade: {row[2]:2s} point: {row[3]}")
def total_credit(table):
    res = [row[1] for row in table]
    print(f"Total credits = {sum(res)}")
    return sum(res)
def cal_gpa(table):
    res = []
    for row in table:
        res.append(row[1]*row[3])
    return sum(res)
file_name = input("Enter grade file: ")
table = read_table(file_name)
print_table(table)
#total_credit(table)
print(f"GPA = {cal_gpa(table)/total_credit(table):.2f}")
'''
'''
#4
file_name = input("Enter age file: ")
file_data = open(file_name).read().splitlines()
new_file_data = [x for x in file_data if x != ""]
#print(new_file_data)
name_list = []
age_list = []
for i in range(len(new_file_data)):
    temp_name,temp_age = new_file_data[i].split(',')
    name_list.append(temp_name)
    age_list.append(temp_age)
#print(name_list)
#print(age_list)
#for row in new_file_data:
    #age_list.append(int(row[1]))
#index_age = age_list.index(max(age_list))
oldest_age = max(age_list)
print(f"Oldest person(s) with the age of {max(age_list)}:")
for i in range(len(name_list)):
    if oldest_age == age_list[i]:
        print(f"- {name_list[i]}")
'''


'''
#5
num = int(input("Number of inputs: "))
input_list = []
name_list = []
for i in range(num):
    input_data = input().split()
    input_list.append(input_data)
print(input_list)
for x in input_list:
    name_list.append(x[0])
print(name_list)

while True:
    student_input = input("student: ") 
    if student_input == "":
        print("End")
        break
    student_input_index = name_list.index(student_input)
    print(f"{input_list[student_input_index][0]}'s score is {input_list[student_input_index][1]}")
#print(input_list)
'''
'''
#6
def read_txt_file():
    animal = int(input("How many animals are there in the zoo? : "))
    name_list = []
    food_list = []
    for i in range(animal):
        temp_name,temp_food = input().split()
        name_list.append(temp_name)
        food_list.append(temp_food)
    return name_list,food_list
def ask(name_list,food_list,temp_ask):
    for i in range(len(name_list)):
        if temp_ask == name_list[i]:
            print(f"{food_list[i]}")
    if temp_ask not in name_list   :
        print("Sorry we don't have that animal.")

name_list,food_list = read_txt_file()
askk = int(input("How many questions do you want to ask? : "))
for i in range(askk):
    temp_ask = input()
    ask(name_list, food_list,temp_ask)
'''
'''
#7
exam_dict = {}
attemp = 1
name_list = []
n = int(input("Number of inputs: "))
for i in range(n):
    name = input("Input name: ")   
    score = float(input("Input score: ")) 
    name_list.append(name)
    if name in exam_dict.keys():

        exam_dict[name]+=score
            
    else:
        exam_dict[name] = score
print(exam_dict)
new_name_list = list(exam_dict.keys())
count_name = []
for i in exam_dict.keys():
    count_name.append(name_list.count(i))
highest_score_name = new_name_list[0]
highest_score = exam_dict[new_name_list[0]]/count_name[0]
for name in range(len(new_name_list)):
    temp_score = exam_dict.get(new_name_list[name])/count_name[name]
    if temp_score > highest_score:
        highest_score_name = new_name_list[name]
        highest_score = temp_score
print(f"Top score is {highest_score_name}: {highest_score:.2f}")
#print(exam_dict)
#print(name_list)
#print(count_name)
'''

'''
#8
file_name = input("File name: ")
file_data = open(file_name).read().splitlines()
new_file_data = [x for x in file_data if x != ""]
#print(new_file_data)
name_list = []
score_list = []

for i in range(len(new_file_data)):
    list_split = new_file_data[i].split(' ')
    name_list.append(list_split[0])
    score_list.append(list_split[1:])
print(score_list)
for i in range(len(score_list)):
    for j in range(len(score_list[i])):
        score_list[i][j] = int(score_list[i][j])
sum_list = []
for i in range(len(score_list)):
    score_list[i].remove(min(score_list[i]))
    score_list[i].remove(max(score_list[i]))
    sum_list.append(sum(score_list[i]))
print(max(sum_list))

for j in range(len(sum_list)):
    if sum_list[j] == max(sum_list):
        print(name_list[j])

#print(score_list)
#Text1.txt
    
#print(name_list) ['Non', 'Prince', 'Khanun', 'Plapud', 'Queen']
#print(score_list) [[9, 8, 7, 8, 8], [3, 5, 4, 2, 10], [7, 7, 9, 9, 6], [0, 9, 7, 8, 10], [10, 7, 7, 8, 7]] 
'''
'''
from typing import List, Union


class Data:
    def __init__(self,name:str,score:int) -> None:
        self.name = name
        self.score = score

    def get_name(self) -> str:
        return self.name

    def get_score(self) -> int:
        return self.score

def read_txt_file() -> List[Union[str,int]]:
    file_name = input("File name: ")
    text_lines = open(file_name).read().splitlines()
    return text_lines

def make_data(text_list:List[Union[str,int]]) -> List[Data]:
    data_list = []
    for i in range(len(text_list)):
        split_index = text_list[i].find(' ')
        name = text_list[i][0:split_index]
        score_list = [int(x) for x in text_list[i][split_index+1:].split(' ')]
        total_score = sum(score_list) - min(score_list) - max(score_list)
        data_list.append(Data(name=name,score=total_score))
    return data_list

def find_highest_score(data_list:List[Data]) -> int:
    highest_score =  data_list[0].get_score()
    for i in range(1,len(data_list)):
        if data_list[i].get_score() > highest_score:
            highest_score = data_list[i].get_score()
    return highest_score

def display(data_list:List[Data],highest_score:int) -> None:
    print(highest_score)
    for i in range(len(data_list)):
        if data_list[i].get_score() == highest_score:
            print(data_list[i].get_name())

text_list = read_txt_file()
data_list = make_data(text_list=text_list)
highest_score = find_highest_score(data_list=data_list)
display(data_list=data_list,highest_score=highest_score)
'''
#9


'''
#10
def read_txt_file():
    file_name = input("File name: ")
    text_lines = open(file_name).read().splitlines()
    return text_lines

def split_text_into_two_part(text_list):
    split_index = 0
    if text_list[0] == "Price":
        for i in range(len(text_list)):
            if text_list[i] == "List":
                split_index = i
        food_data_list = text_list[1:split_index]
        buy_list = text_list[split_index+1:]

    if text_list[0] == "List":
        for i in range(len(text_list)):
            if text_list[i] == "Price":
                split_index = i
        food_data_list = text_list[split_index+1:]
        buy_list = text_list[1:split_index]
    return food_data_list,buy_list

def make_food_list_to_dict(food_data_list):
    food_data_dict = {}
    for i in range(len(food_data_list)):
        name,price = food_data_list[i].split(' ')
        food_data_dict[name] = int(price)
    return food_data_dict

def display_txt_data(text_list) :
    for text in text_list:
        print(text)

def calculate_total_price(food_data_dict,buy_list):
    total_price = 0 
    for i in range(len(buy_list)):
        name,amount = buy_list[i].split(' ')
        temp_price = food_data_dict.get(name)
        if name in food_data_dict.keys():
            total_price += int(amount)*temp_price
    return total_price

text_list = read_txt_file()
food_list,buy_list = split_text_into_two_part(text_list)
food_dict = make_food_list_to_dict(food_list)
display_txt_data(text_list)
print("Total price: {}".format(calculate_total_price(food_dict,buy_list)))
'''
#11
'''
from typing import List


class Data:
    def __init__(self,number:int,data:str) -> None:
        self.number = number
        self.data = data
    
    def display_data(self) -> None:
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print(self.data[i][j],end='')
            print()
        
    def get_number(self) -> int:
        return self.number

def read_txt_file():
    file_name = input("File name: ")
    text_lines = open(file_name).read().splitlines()
    return text_lines

def make_and_sort_Data(text_list:List) -> List[Data]:
    number_list = [int(x) for x in range(10)]
    temp_list = []
    data_list = []
    number = int(text_list[0])
    for i in range(len(text_list)):
        if len(text_list[i]) == 1 and int(text_list[i]) in number_list:
            if i != 0:
                data_list.append(Data(number=number,data=temp_list))
                temp_list = []
                number = int(text_list[i])
        else:
            temp_list.append(list(text_list[i]))
    data_list = sorted(data_list,key=lambda data:data.get_number())
    return data_list

text_list = read_txt_file()
data_list = make_and_sort_Data(text_list)
for i in range(len(data_list)):
    data_list[i].display_data()'''

'''

 #11 เเบบที่สอง
file_name=input('File name: ')
file_data=open(file_name).read().splitlines()
pic=[]
temp=[]
#print(file_data)
for i in range(len(file_data)):
    if not file_data[i].isdigit():
        temp.append(file_data[i])
    else:
        if temp!=[]:
            pic.append(temp)
        temp=[]
    #print(temp)
print(pic)
#print(pic)
seq=[int(i) for i in file_data if i.isdigit() and int(i)!=0]
#print(seq)
tempp={}
for i in range(len(pic)):
    tempp[seq[i]]=pic[i]
#print(tempp)
for i in sorted(list(tempp.keys())):
    for j in range(len(tempp[i])):
        print(tempp[i][j])
'''

'''
#12
def read_txt_file():
    file_name = input("File name: ")
    text_lines = open(file_name).read().splitlines()
    return text_lines
def split_sentence(text_list):
    new_split_sentence = text_list[0].split('.')
    return new_split_sentence
def split_word(text_list):
    new_split_word = text_list[0].split(' ')
    return new_split_word
text_list = read_txt_file()
#print(len(split_sentence(text_list))-1)
#print(len(split_word(text_list)))
print(f"There are {len(split_sentence(text_list))-1} sentences and {len(split_word(text_list))} words.")
'''
'''
#13
def read_txt_file():
    file_name = input("file name: ")
    text_lines = open(file_name).read().splitlines()
    return text_lines
def check_computer(text_list):
    count = 0
    for i in range(len(text_list)):
        temp = text_list[i].lower()
        count += temp.count("computer")
    return count
text_list = read_txt_file()
print(f"Count = {check_computer(text_list)}")
'''
'''
def find_gcd(base,divide):
    remain = base % divide
    while remain != 0 :
        base = divide
        divide = remain
        remain = base % divide
    return divide
def find_lcm(a,b,gcd):
    return a*b//gcd
number1 = int(input("a : "))
number2 = int(input("b : "))
if number1 < number2:
    number2,number1 = number1,number2
gcd = find_gcd(number1, number2)
lcm = find_lcm(number1, number2, gcd)
print(f"GCD : {gcd}")
print(f"LCM : {lcm}")
'''
'''
import math
def find_gcd(base,divide):
    return math.gcd(base, divide)
def find_lcm(a,b):
    return math.lcm(a,b)
number1 = int(input("a : "))
number2 = int(input("b : "))
if number1 < number2:
    number2,number1 = number1,number2
gcd = find_gcd(number1, number2)
lcm = find_lcm(number1, number2)
print(f"GCD : {gcd}")
print(f"LCM : {lcm}")
'''
#16
'''
max_length = 0
length = 1
word_chain = 0
text = input("Text: ").split()
text.append(list(['-']*len(text[0])))
#lis.append(text)
for i in range(1,len(text)):
    count = 0
    for j in range(len(text[i])):
        #print(text[i][j])
        if text[i][j] != text[i-1][j]:
            count+=1
    #print(count)
    if count<=2:
        length+=1
           
    else:
        if length > max_length:
            max_length = length
        length = 1
        word_chain += 1
                

print(f"{word_chain} Chain(s). Maximum length is {max_length} word(s).")
            
#print(word_chain)
#print(count)
#print(lis)
'''

'''
#17
n = int(input("N : "))
weigh_dict = {}
for i in range(n):
    name,weight = input().split()
    weigh_dict[name] = int(weight)
res = input()
name_res = res.split('+')
for i in range(len(name_res)):
    name_res[i] = name_res[i].strip()
result = 0
for i in name_res:
    result += weigh_dict.get(i)
print(result) 
'''

