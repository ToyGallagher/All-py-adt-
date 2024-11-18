#1
'''
def getinput():
    num = int(input())
    return num
def numinput(num):
    num1 = []
    num2 = []
    for i in range(num):
        first = input().split(',')
        second = input().split(',')
    for j in first:
        j = int(j)
        num1.append(j)
    for k in second:
        k = int(k)
        num2.append(k)
    return num1,num2
def cal(num1,num2):
    newnum1 = []
    newnum2 = []
    calnum1 = 0
    calnum2 = 0
    for i in range(min(num1),max(num1)):
        newnum1.append(i)
    for i in range(min(num2),max(num2)):
        newnum2.append(i)
    for j in newnum1:
        if j not in num1:
            calnum1+=j
    for j in newnum2:
        if j not in num2:
            calnum2+=j
    return calnum1,calnum2
def show(calnum1,calnum2):
    print(calnum1)
    print(calnum2)
    
num = getinput()
num1,num2 = numinput(num)
print(cal(num1, num2))

'''
'''
n = int(input())

for i in range(n):
    temp = []
    myinput = input().split(',')
    for j in myinput:
        j = int(j)
        temp.append(j)
    tempsum = 0
    for num in range(min(temp),max(temp)):
        if num not in temp:
            tempsum+=num
    print(tempsum)
    '''
'''
#2
n = int(input())
for i in range(n):
    list_word = []
    curr_word = 0
    word = input()
    for j in range(len(word)):
        list_word.append(word[j])
    for k in range(len(list_word)):
        if list_word[k]!=" ":
            if curr_word%2 == 0:
                list_word[k] = list_word[k].upper()
            else:
                list_word[k] = list_word[k].lower()
            curr_word += 1
    for p in range(len(list_word)):
        print(list_word[p],end = '')
    print()
'''       

#3
'''
n = int(input())
for i in range(n):
    x = input()
    half = len(x)//2
    #for i in range(0,half):
    new1 = ""
    new1 += x[half-1::-1]
    #print(new1)
    #for j in range(half+1,len((x))):
    new2 = ""
    new2 += x[len(x):half-1:-1]
    #print(new2)
    print(new1+new2)
'''
'''
#4
word_list = input().split()
hash_value = 0
x = []
for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        x.append(word_list[i][j])
        #print(word_list[i][j])
        hash_value+=ord(word_list[i][j].upper())-65+j
print(hash_value)
'''


#5
'''
#6
lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst.append(0)

max_high = max(lst)
max_area = 0
for i in range(1,max_high+1):
    temp_longest_lst = 0
    for j in range(len(lst)):
        if lst[j] >= i:
            temp_longest_lst += 1
        else:
            if temp_longest_lst*i > max_area:
                max_area = temp_longest_lst*i
            temp_longest_lst = 0
print(max_area)'''
#7
'''
floor = [int(x) for x in input().split()]
curr_floor = int(input())

total_move = 0
while len(floor) > 0 :
    min_move = abs(floor[0]-curr_floor)
    floor_index = 0
    for i in range(1,len(floor)):
        if abs(floor[i]-curr_floor) < min_move:
            min_move = abs(floor[i]-curr_floor)
            floor_index = i
    total_move += min_move
    curr_floor = floor[floor_index]
    floor.pop(floor_index)

print(total_move)
'''
#8
'''
n = int(input())
x , y = [],[]
for i in range(n):
    inpx , inpy =[int(x) for x in input().split()]
    x.append(inpx)
    y.append(inpy)
newx , newy =[int(x) for x in input().split()]
totalcal = int(input())
result_list = []
for i in range(n):
    temp_result = ((newx - x[i])**2 + (newy - y[i])**2)**0.5
    result_list.append(temp_result)
result_list.sort()
for i in range(totalcal):
    print(f"{result_list[i]:.2f}")
'''
#9
'''
word_list = input().split(',')
for i in range(len(word_list)):
    print(f'"{word_list[i].strip()}"',end='')
    if i != len(word_list)-1:
        print(',',end='')
'''
#11
'''
import math
ammo_damage = int(input())
zombie_hp = [int(x) for x in input().split()]
ammo_use = []
ammo_use.append(math.ceil(zombie_hp[0]/ammo_damage))
for i in range(1,len(zombie_hp)):
    ammo_use.append(math.ceil(zombie_hp[i]/ammo_damage)+ammo_use[i-1])
print(ammo_use[-1])
for i in ammo_use:
    print(i,end = ' ')
'''
#13
'''
string = input()
postion_index = int(input())
new_character = input()
print(string[:postion_index] + new_character + string[postion_index+1:])
'''
'''
import json
from typing import Dict, List

class TwitterData:
    def __init__(self,tweet_id,author,filtering,topic,topic_priority,language,text) -> None:
        self.tweet_id = tweet_id
        self.author = author
        self.filtering = filtering
        self.topic = topic
        self.topic_priority = topic_priority
        self.language = language
        self.text = text
    
    def get_author(self) -> str:
        return self.author
    def get_topic(self) -> str:
        return self.topic
    def get_topic_priority(self) -> str:
        return self.topic_priority
    def get_languagle(self) -> str:
        return self.language
    def get_total_word(self) -> int:
        space = 0
        for i in range(len(self.text)):
            if self.text[i] == ' ':
                space += 1
        return space + 1

def read_json_file(filename:str) -> List[Dict]:
    f = open(filename)
    data_list = json.load(f)
    f.close()
    return data_list

def make_TwitterData_list(data_list:List[Dict]) -> List[TwitterData]:
    twitterData_list = []
    for data in data_list:
        twitterData_list.append(TwitterData(data["tweet_id"],data["author"],data["filtering"]\
            ,data["topic"],data["topic_priority"],data["language"],data["text"]))
    return twitterData_list

def find_total_tweet(twitterData_list:List[TwitterData]) -> int:
    return len(twitterData_list)

def display_highest_tweet(tweet_dict:Dict[str,int],highest_tweet) -> None:
    for author,tweet in tweet_dict.items():
        if tweet == highest_tweet:
            print(author)

def find_total_twitterAc(twitterData_list:List[TwitterData],option:int) -> None:
    tweet_dict = {}
    firstTime = True
    for twitterData in twitterData_list:
        author = twitterData.get_author()
        if author in tweet_dict:
            tweet_dict[author] += 1
            if tweet_dict[author] > highest_tweet:
                highest_tweet = tweet_dict[author]
        else:
            tweet_dict[author] = 1
            if firstTime:
                highest_tweet = 1
                firstTime = False

    if option == 1:
        print(len(tweet_dict))
    if option == 2:
        display_highest_tweet(tweet_dict,highest_tweet)

def find_total_topic(twitterData_list:List[TwitterData]) -> int:
    topic_dict = {}
    for twitterData in twitterData_list:
        topic = twitterData.get_topic()
        if topic in topic_dict:
            topic_dict[topic] += 1
        else:
            topic_dict[topic] = 1
    return len(topic_dict)

def find_topic_priority_with_option(twitterData_list:List[TwitterData],option:int) -> int:
    total_find_topic_priority = 0
    for twitterData in twitterData_list:
        topic_priority = twitterData.get_topic_priority()
        if option == 1 and topic_priority == "ALERT":
            total_find_topic_priority += 1
        if option == 2 and topic_priority == "UNIMPORTANT":
            total_find_topic_priority += 1
    return total_find_topic_priority

def have_other_language(twitterData_list:List[TwitterData]) -> bool:
    for twitterData in twitterData_list:
        language = twitterData.get_languagle()
        if language != "EN":
            return True
    return False

def find_highest_length_text(twitterData_list:List[TwitterData]) -> int:
    highest = 0
    firstTime = True
    for twitterData in twitterData_list:
        length_text = twitterData.get_total_word()
        if firstTime:
            highest = length_text
            firstTime = False
        if length_text > highest:
            highest = length_text
    return highest
            
filename = input("File Name: ")
data_list = read_json_file(filename=filename)
twitterData_list = make_TwitterData_list(data_list=data_list)
choice = int(input("input: "))

if choice == 1:
    print(find_total_tweet(twitterData_list))
if choice == 2:
    find_total_twitterAc(twitterData_list,1)
if choice == 3:
    find_total_twitterAc(twitterData_list,2)
if choice == 4:
    print(find_total_topic(twitterData_list))
if choice == 5:
    print(find_topic_priority_with_option(twitterData_list,1))
if choice == 6:
    print(find_topic_priority_with_option(twitterData_list,2))
if choice == 7:
    print(have_other_language(twitterData_list))
if choice == 8:
    print(find_highest_length_text(twitterData_list))'''
row=int(input('Enter Rook\'s row position: '))
column=int(input('Enter Rook\'s column position: '))
rtable=['| ','| ','| ','| ','| ','| ','| ','| |']
print('-----------------')
for i in range(8):
    for j in range(8):
        if i==row and j==column:
            print(rtable[j].replace(' ','R'),end='')
        elif i==row or j==column:
            print(rtable[j].replace(' ','x'),end='')
        else:
            print(rtable[j],end='')
    print('\n-----------------')