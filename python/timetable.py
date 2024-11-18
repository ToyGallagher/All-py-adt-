from typing import List, Dict

class Subject:
    def __init__(self,name:str,code:str,total_sec:int) -> None:
        self.name = name
        self.code = code
        self.total_sec = total_sec
        self.sec_data = []
    
    def __repr__(self) -> str:
        return f"name({self.name}), code({self.code})"

    def append_sec(self,sec_code:str,data:List[List]) -> None:
        self.sec_data.append([sec_code,data])
    
    def get_total_sec(self) -> int:
        return self.total_sec

    def get_sec_data(self,index:int) -> List:
        return self.sec_data[index]

def get_input_manual():
    subjectData_list = []
    total_subject = int(input("Total subject: "))
    for i in range(total_subject):
        subject_code = input("Subject Code (ex. 01204114-65): ")
        subject_name = input("Subject Name (ex. Introduction to Computer Hardware Development): ")
        total_sec = int(input("Total sec: "))
        subjectData = Subject(subject_name,subject_code,total_sec)
        for j in range(total_sec):
            sec = input("Sec: ")
            sec_time_list = []
            total_day = int(input("Total day in this sec: "))
            for k in range(total_day):
                day,time_range = input("Day : Time range (ex. MON 9:00-12:00): ").split(' ')
                start_time,end_time = time_range.split('-')
                temp_list = [day,start_time,end_time]
                sec_time_list.append(list(temp_list))
            subjectData.append_sec(sec,sec_time_list)
        subjectData_list.append(subjectData)
    return subjectData_list

def get_input_file():
    pass

def make_time_table(time_range="8:00-20:00") -> Dict[str,List]:
    start_time,end_time = time_range.split('-')
    sH,sM = start_time.split(':')
    sH,sM = int(sH),int(sM)
    eH,eM = end_time.split(':')
    eH,eM = int(eH),int(eM)
    if sM == 30:
        sH += 0.5
    if eM == 30:
        eH += 0.5

    time_table = []
    while sH <= eH:
        time_table.append(0)
        sH += 0.5
    return time_table

def make_day_table(time_table:List[int]) -> Dict[str,List[int]]:
    day_list = ["MON","TUE","WED","THU","FRI","SAT"]
    day_dict = {}
    for day in day_list:
        day_dict[day] = time_table
    return day_dict

def reset_day_table(time_table:List[int]):
    global day_dict
    day_list = ["MON","TUE","WED","THU","FRI","SAT"]
    for day in day_list:
        day_dict[day] = time_table

def place_subject_in_table(subjectData_list:List[Subject],index_list:List[int]):
    global day_dict
    DEFAULT_SH = 8
    for i in range(len(index_list)):
        sec_data = subjectData_list[i].get_sec_data(index_list[i])
        temp_data = sec_data[1]
        for j in range(len(temp_data)):
            temp_day = temp_data[j][0]
            start_time,end_time = temp_data[j][1],temp_data[j][2]
            temp_time_list = list(day_dict[temp_day])
            sH,sM = start_time.split(':')
            sH,sM = int(sH),int(sM)
            eH,eM = end_time.split(':')
            eH,eM = int(eH),int(eM)
            if sM == 30:
                sH += 0.5
            if eM == 30:
                eH += 0.5
            while sH < eH:
                if temp_time_list[int((sH-DEFAULT_SH)//0.5)] == 1:
                    return False
                else:   
                    temp_time_list[int((sH-DEFAULT_SH)//0.5)] = 1
                sH += 0.5
            day_dict[temp_day] = temp_time_list
            # global count
            # print(sec_data[0],temp_day,start_time,end_time,"count =",count)
            # display_time()
            # print()
            # count += 1
    return True
            
def display_time():
    global day_dict
    for day,time in day_dict.items():
        print(day,end=' ')
        print(time)
        
def find_schedule(subjectData_list:List[Subject]):
    global day_dict,time_table
    #setup
    result_list = []
    index_list = [0]*len(subjectData_list)
    max_index_list = []
    for i in range(len(subjectData_list)):
        max_index_list.append(subjectData_list[i].get_total_sec())
    point_index = len(subjectData_list)-1

    while True:
        temp_result = place_subject_in_table(subjectData_list,index_list)
        reset_day_table(time_table)
        # print(point_index)
        if temp_result == True:
            result_list.append(list(index_list))
        # print(index_list,max_index_list)
        index_list[point_index] += 1
        while index_list[point_index] == max_index_list[point_index]:
            index_list[point_index] = 0
            point_index -=1
            if point_index == -1:
                return result_list
            index_list[point_index] += 1
        point_index = len(subjectData_list)-1

def display_result(subjectData_list:List[Subject],result_list:List[List[int]]) -> None:
    if result_list != 0:
        print(f"\nAll {len(result_list)} schedule possible")
        for i in range(len(result_list)):
            print("---------------------------")
            print(f"Schedule #{i+1}")
            for j in range(len(subjectData_list)):
                print(subjectData_list[j].code,subjectData_list[j].name)
                temp_data = subjectData_list[j].get_sec_data(result_list[i][j])
                print("Sec: {}".format(temp_data[0]))
                for k in range(len(temp_data[1])):
                    print(temp_data[1][k][0],temp_data[1][k][1],'-',temp_data[1][k][2]) 
                print()
            print("---------------------------\n")
    else:
        print("\nNo schedule possible")


# subjectData_list = [Subject("333","4444",3),Subject("333","4444",2)]
time_table = make_time_table()
day_dict = make_day_table(time_table)
option = int(input("Input data from (1)manual (2)file: "))
if option == 1:
    subjectData_list = get_input_manual()
if option == 2:
    subjectData_list = get_input_file()
result_list = find_schedule(subjectData_list)
display_result(subjectData_list,result_list)