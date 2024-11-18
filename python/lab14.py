'''
#1
import csv
maxx = 1
minn = 0

def read_csv(filename):
    #f = open(filename).read().splitlines()
    #print(f)
    
    
    with open(filename) as f:
        
        global maxx , minn
        
        #datas = csv.reader(f)
        #data = [ i for i in datas]
        
        data=[]
        lis = []
        for i in f.read().splitlines():
            data.append(i.split(','))
        #print(data)
    #for i in range(1,len(data)) :
        #maxx = max(maxx,int(data[i][6]))
        #minn = min(minn,int(data[i][7]))
        #print(maxx,minn)
        maxlist = []
        minlist = []
        for i in range(1,len(data)):
            maxlist.append(int(data[i][6]))
            minlist.append(int(data[i][7]))
            maxx = max(maxlist)
            minn = min(minlist)
    return  data
class Std:
    def __init__(self,id,gender,race,level,lunch,test,math,reading,writing):
        self.id = id
        self.gender = gender
        self.race = race
        self.level = level
        self.lunch = lunch
        self.test = test
        self.math = int(math)
        self.reading = int(reading)
        self.writing = int(writing)
    def __str__(self) -> str:
        return f"math score : {self.math}, reading score : {self.reading}, writing score : {self.writing}"
    def show_data(self):
        print(f"gender : {self.gender}")
        print(f"race/ethnicity : {self.race}")
        print(f"parental level of education : {self.level}")
        print(f"lunch : {self.lunch}")
        print(f"test preparation course : {self.test}")
        print(f"math score : {self.math}")
        print(f"reading score : {self.reading}")
        print(f"writing score : {self.writing}")
    def less_from_max_math_score(self):
        print(f"less than max : {maxx - self.math}")
    def more_from_min_reading_score(self):
        print(f"more than min : {self.reading - minn}")
    def can_pass(self):
        total_score = self.math + self.reading + self.writing
        if total_score > 240:
            print("Pass")
        else:
            print("Can't pass")

filename = input("Filename : ")
datas = read_csv(filename)
classes = list()
for i in range(1,len(datas)) :
    data = Std(datas[i][0],datas[i][1],datas[i][2],datas[i][3],datas[i][4],datas[i][5],datas[i][6],datas[i][7],datas[i][8])
    classes.append(data)
#print(classes)

menu = int(input("Menu : "))
id = input("ID : ")
for i in classes :
    if i.id == id :
        if menu == 1 : # show data
            i.show_data()
        elif menu == 2 : # less_from_max_math_score
            i.less_from_max_math_score()
        elif menu == 3 : # more_from_min_reading_score
            i.more_from_min_reading_score()
        elif menu == 4: # can_pass
            i.can_pass()
        elif menu == 5: # print
            print(i)
        break

'''
'''
#2
import json
class Account:
    def __init__(self,account_number):
        self.account_number = account_number
    def show_data(self):
        print()
        print(f"Account number : {self.account_number}")



   

filename = input("Filename : ")
with open(filename) as f:
    f = f.read()
    x = json.loads(f)
    #print(x)
account_number = input("Account number : ")
for i in range(len(x)):
    if account_number == x[i]["account number"]:

    #print(x[i]["account number"])

       '''
'''
#3
import json
from typing import List, Dict

def read_json_file() -> List[Dict]:
    file_name = input("Enter json filename : ")
    f = open(file_name)
    data = json.load(f)
    data_list = data["racer"]
    f.close()
    return data_list
def calculate_time(distance:int,range_list:List[int],velocity_list:List[int]) -> float:
    time = 0
    if len(range_list) == 1:
        time = float(distance)/float(velocity_list[0])
    else:
        condition = True
        for i in range(1,len(range_list)):
            if range_list[i] > distance:
                temp_range = distance - range_list[i-1]
                time = time + float(temp_range)/float(velocity_list[i-1])
                condition = False
                break
            else:
                temp_range = range_list[i] - range_list[i-1]
                time = time + float(temp_range)/float(velocity_list[i-1])
        if condition:
            temp_range = distance - range_list[-1]
            time = time + float(temp_range)/float(velocity_list[-1])
    return time
'''
'''
#4
class Item:
    def __init__(self,id,type,price):
        self.id = id
        self.type = type
        self.price = price
    def getType(self):
        return self.type
    def getPrice(self):
        return self.price
def whatisid(id,res):
    return res[id].getType()
def whatisprice(id,res):
    return res[id].getPrice()
def get_input():
    item_dict = {}
    total_item = int(input("How many products are there? : "))
    for i in range(total_item):
        temp_id,temp_type,temp_price = input().split()
        item_temp = Item(temp_id,temp_type,temp_price)
        item_dict[temp_id] = item_temp
        #print(item_dict)
    return item_dict
def main(res):
    cont = True
    while cont:
        id = input("Id : ")
        if id not in res.keys():
            print("This id doesn't exist.")
        else:
            while True:
                q = int(input("Q : "))
                if q == 1:
                    print(whatisid(id, res))
                elif q == 2:
                    print(whatisprice(id, res))
                elif q == 3:
                    break
                elif q == 0:
                    cont = False
                    break

res = get_input()
main(res)
'''
    
'''
#5
import csv
class Country:
    nbCountry = 0
    def __init__(self, country, population, EU,coastline):
        self.country = country
        self.population = float(population)
        self.EU = EU
        self.coastline = coastline
        Country.nbCountry += 1
    def get_coastline(self):
        return  self.coastline
    def get_EU(self):
        return self.EU
    def get_country(self):
        return self.country
    def get_population(self):
        return self.population

   

filename = input("Enter File name: ")
datas = open(filename).read().splitlines()
classes = list()
for i in range(1,len(datas)):
    data = datas[i].split(',')
    data[1] = float(data[1])
    opdata = Country(data[0],data[1],data[2],data[3])
    if opdata.get_EU() == 'no' and opdata.get_coastline() == 'yes':
        print(opdata.get_country(),opdata.get_population())
#print(coastline(data))    
#classes.append(data)
#print(classes)
'''
'''
#6
class City:
  nbCity = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1
file_name = input('Enter file name: ')
data = open(file_name).read().splitlines()
#print(data)
temp = []
for i in range(1,len(data)):
    datas = data[i].split(',')
    print(datas)
    temp.append(datas[4])
    temp = [float(x) for x in temp]
print(f'Minimum: {min(temp):.2f}')
print(f'Maximum: {max(temp):.2f}')
print(f'Average temperature: {sum(temp)/(len(temp)):.4f}')
'''
'''
#7
file_name = input('Enter file name: ')
data = open(file_name).read().splitlines()
#print(data)
temp = []
temp2 = []
country = {}
for i in range(1,len(data)):
    datas = data[i].split(',')
    datas[4] = float(datas[4])
    print(datas)
    temp2.append(datas)
  
    
    if temp2[i-1][1] not in country.keys():
        country[temp2[i-1][1]]=temp2[i-1][4]
        temp.append(temp2[i-1][1])
    else: 
        country[temp2[i-1][1]]+=temp2[i-1][4]
        temp.append(temp2[i-1][1])
for i in country.keys():
    count = temp.count(i)
    #print(count)
    print(f'{i} {country[i]/count:.2f}')
'''
#print(temp2)
#print(country)
#print(temp)



'''
#8
city_file = 'Cities.csv'
country_file = 'Countries.csv'
city_data = open(city_file).read().splitlines()
country_data = open(country_file).read().splitlines()
country_list = []
new_country_list = []

city_list = []
name_country_list = []
for i in range(1,len(country_data)):
    new_country = country_data[i].split(',')
    country_list.append(new_country)
    name_country_list.append(new_country[0])
    if new_country[2] == 'no' and new_country[3] == 'yes':
        #print(new_country[0],new_country[1])
        new_country_list.append(new_country[0])
#print(name_country_list)
#print(city_data)
#print(country_list)
#print(country_list)
#print(new_country_list)
#print('-------------------------------------------------')
city_dict = {}
for i in range(1,len(city_data)):
    new_city = city_data[i].split(',')
    city_list.append(new_city)
#print(len(city_list))
for i in range(1,len(city_list)):
    if city_list[i-1][1] in name_country_list:
        if city_list[i-1][1] not in city_dict.keys():
            city_dict[city_list[i-1][1]]=city_list[i-1][4]
            #temp.append(temp2[i-1][1])
        elif city_list[i-1][1] in city_dict.keys():
            city_dict[city_list[i-1][1]]+=city_list[i-1][4]
            #temp.append(temp2[i-1][1])
#print(country_list)
    #print(new_city)
#print(city_dict)

print('Average temperature of countries having coastline, but not in EU:')
for i in range(len(new_country_list)):
    print(f'{new_country_list[i]} {city_dict[country_list[i]]}')
#for i in range(len(country_list)):
    #print(country_list[i],new_city[i][4])
'''
'''
#9
import json
file_name = input("File Name: ")
with open(file_name) as f:
    data = json.load(f)

#file_name = input("File name: ")
#file_data = open(file_name)
#data = json.load(file_data)
#file_data.close()
#print(data)
temp = int(input('Input : '))
if temp == 1 :
    print(len(data))
elif temp == 2:
    total = 0
    for i in data:
        total+=int(i['population'])
    print(total)
elif temp == 3:
    c_country = 0
    for i in data:
        if i['country'][0] == 'C':
            c_country+=1
    print(c_country)
    five_country = 0
    for i in data:
        if len(i['country'])>5:
            five_country+=1
    print(five_country)
elif temp == 4:
    count1=0
    for i in data:
        if int(i['population'])>500000000:
            count1+=1
    print(count1)
    count2=0
    for i in data:
        if 250000000<=int(i['population'])<=750000000:
            count2+=1
    print(count2)
    count3=0
    for i in data:
        if int(i['population'])<10000000:
            count3+=1
    print(count3)
elif temp == 5:
    top20 = 0
    top = 0
    for i in data:
        if int(i['Rank'])<=20:
            top20+=float(i['World'])
        elif 50<=int(i['Rank'])<=150:
            top+=float(i['World'])
    print(f'{top20*100:.2f}')
    print(f'{top*100:.2f}')
'''



'''
#9 nuk
import json
from typing import Dict, List, Tuple

class CountryData:
    def __init__(self,rank:int,country:str,population:int,world:float) -> None:
        self.rank = rank
        self.country = country
        self.population = population
        self.world = world

    def __repr__(self) -> str:
        return f"rank={self.rank}. country={self.country}. population={self.population}. world={self.world}"       

    def get_country(self) -> str:
        return self.country

    def get_population(self) -> int:
        return self.population

    def get_world(self) -> float:
        return self.world

def read_json_file(filename:str) -> List[Dict]:
    f = open(filename)
    data_list = json.load(f)
    f.close()
    return data_list

def make_CountryData_list(data_list:List[Dict]) -> List[CountryData]:
    countryData_list = []
    for i in range(len(data_list)):
        data = data_list[i]
        countryData_list.append(CountryData(int(data["Rank"]),data["country"],int(data["population"]),float(data["World"])))
    return countryData_list

def find_total_country(countryData_list:List[CountryData]) -> int:
    return len(countryData_list)

def find_total_population(countryData_list:List[CountryData]) -> int:
    total_population = 0
    for countryData in countryData_list:
        total_population = total_population + countryData.get_population()
    return total_population

def find_countryFirstChrC_and_lenMoreThan5(countryData_list:List[CountryData]) -> Tuple[int,int]:
    total_countryFirstChrC = 0
    total_countryLenMoreThan5 = 0
    for countryData in countryData_list:
        country_name = countryData.get_country()
        if country_name[0] == 'C':
            total_countryFirstChrC += 1
        if len(country_name) > 5:
            total_countryLenMoreThan5 += 1
    return total_countryFirstChrC,total_countryLenMoreThan5

def find_populataion_with_option(countryData_list:List[CountryData]) -> Tuple[int,int,int]:
    total_CPMT500Mil = 0 # Country population more than 500 millions
    total_CPrange250_750Mil = 0 # Country population in range(250,750) millions
    total_CPLT10Mil = 0 # Country population less than 10 millions
    for countryData in countryData_list:
        population = countryData.get_population()
        if population > 500000000:
            total_CPMT500Mil += 1
        if population > 250000000 and population < 750000000:
            total_CPrange250_750Mil += 1
        if population < 10000000:
            total_CPLT10Mil += 1
    return total_CPMT500Mil,total_CPrange250_750Mil,total_CPLT10Mil

def find_population_percent_in_range(countryData_list:List[CountryData]) -> float:
    population_percent = 0
    for countryData in countryData_list:
        population_percent += countryData.get_world()
    return population_percent*100

def find_population_percent_with_option(countryData_list:List[CountryData]) -> Tuple[float,float]:
    percent_populationRankrange1_20 = find_population_percent_in_range(countryData_list[0:20])
    percent_populationRankrange50_150 = find_population_percent_in_range(countryData_list[49:149])
    return percent_populationRankrange1_20,percent_populationRankrange50_150

filename = input("File Name: ")
data_list = read_json_file(filename=filename)
countryData_list = make_CountryData_list(data_list=data_list)
command = int(input("Input : "))

if command == 1:
    print(find_total_country(countryData_list=countryData_list))
if command == 2:
    print(find_total_population(countryData_list=countryData_list))
if command == 3:
    temp = find_countryFirstChrC_and_lenMoreThan5(countryData_list=countryData_list)
    print(f"{temp[0]}\n{temp[1]}")
if command == 4:
    temp = find_populataion_with_option(countryData_list=countryData_list)
    print(f"{temp[0]}\n{temp[1]}\n{temp[2]}")
if command == 5:
    temp = find_population_percent_with_option(countryData_list=countryData_list)
    print(f"{temp[0]:.2f}\n{temp[1]:.2f}")
    '''

#10
'''
import json

file_name=input('File name: ')
#file_name=input('File name: ')

with open(file_name) as f:
    data=json.load(f)

author={} #{ชื่อ,จำนวนทวีต}
topic=[]
alertTopic=0
unimportant=0
eng=False
max_length=0

for i in data:
    #author
    
    if i['author'] not in author:
        #author.update({i['author']:1})
        author[i['author']] = 1 
    
    else:
        author[i['author']]+=1
   
    #topic
    if i['topic'] not in topic:
        topic.append(i['topic'])
    #alert
    if i['topic_priority']=='ALERT':
        alertTopic+=1
    elif i['topic_priority']=='UNIMPORTANT':
        unimportant+=1
    #EN
    if i['language']!='EN':
        eng=True
    #Text lenght
    word=i['text'].split()
    if len(word)>max_length:
        max_length=len(word)
author={i:j for i,j in sorted(author.items(),key=lambda item:item[1],reverse=True)}
#print(author.items())

op=int(input('input: '))
if op==1:
    print(len(data))
elif op==2:
    print(len(author))
elif op==3:
    most=max(list(author.values()))
    for i,j in author.items():
        if j==most:
            print(i)
elif op==4:
    print(len(topic))
elif op==5:
    print(alertTopic)
elif op==6:
    print(unimportant)
elif op==7:
    print(eng)
elif op==8:
    print(max_length) 
'''
'''
choice = input()
round = int(input())
lis = []
reverse_list = []
for i in range(round):
    data = input()
    lis.append(data)
#print(lis)
if choice == '90':
    #for i in range(len(lis),0,-1):
    for i in range(len(lis)-1,-1,-1):
        reverse_list.append(lis[i])
    #print(reverse_list)
    #x = [[reverse_list[j][i] for j in range(len(reverse_list))] for i in range(len(reverse_list[0]))]
    #print(x)
    new=''
    new2= []
    for i in range(len(reverse_list[0])):
        for j in range(len(reverse_list)):
            new+=reverse_list[j][i]
        new2.append(new)
        new = ''
    #print(new2)
    for i in new2:
        print(i)
        
'''

