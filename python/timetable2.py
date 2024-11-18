
from typing import List, Dict
from math import floor, ceil


def editYamlFile(subjectDataDict:Dict[str,str]) -> None:
    path = os.getcwd()
    place = 1
    while True:
        filepath = path + "\schedule{}.yaml".format(place)
        if os.path.exists(filepath):
            place += 1
            if place > 16:
                break
        else:
            with open(r'{}'.format(filepath), 'w') as file:
                yaml.dump(subjectDataDict, file)
            break

class Subject:
    def __init__(self, subjectName:str, subjectCode:str, subjectTotalSection:int) -> None:
        self.subjectName = subjectName
        self.subjectCode = subjectCode
        self.subjectTotalSection = subjectTotalSection
        self.subjectSectionData = {}
    
    def __repr__(self) -> str:
        return f"name({self.subjectName}), code({self.subjectCode})\n{self.subjectSectionData}"

    def appendSectionData(self, sectionCode:str, tempTimeList:List) -> None:
        self.subjectSectionData[sectionCode] = tempTimeList
    
    def getSubjectName(self) -> str:
        return self.subjectName

    def getSubjectTotalSection(self) -> int:
        return self.subjectTotalSection

    def getSubjectSectionData(self) -> Dict[str,List]:
        return self.subjectSectionData


def manualInput() -> List[Subject]:
    subjectList = []
    totalSubject = int(input("Total subject: "))
    for i in range(totalSubject):
        tempSubjectCode = input("Subject Code (ex. 01204114-65): ")
        tempSubjectName = input("Subject Name (ex. Introduction to Computer Hardware Development): ")
        tempSubjectTotalSection = int(input("Total sec (ex. 3): "))

        tempSubject = Subject(tempSubjectName, tempSubjectCode, tempSubjectTotalSection)
        for j in range(tempSubjectTotalSection):
            tempSectionCode = input("Section (ex. 11): ")
            tempTotalDay = int(input("Total day this section has: (ex. 4): "))

            tempTimeList = []
            for k in range(tempTotalDay):
                tempDayName, tempTimeRange = input("Day : TimeRange (ex. MON 9:00-12:00): ").split(' ')
                tempStartTime, tempEndTime = tempTimeRange.split('-')
                tempTimeList.append(list([tempDayName, tempStartTime, tempEndTime]))
            tempSubject.appendSectionData(tempSectionCode, tempTimeList)
        subjectList.append(tempSubject)
        print("------------------------------------------------------------------------------------------------------")
    return subjectList

def fileInput():
    pass

def findLowestStartTime(subjectList:List[Subject]) -> int:
    startTime = None
    for subject in subjectList:
        tempSubjectSectionData = subject.getSubjectSectionData()
        for sectionCode in tempSubjectSectionData.keys():
            for timeList in tempSubjectSectionData.get(sectionCode):
                tempHour, tempMinute = timeList[1].split(':')
                tempHour, tempMinute = int(tempHour), int(tempMinute)
                tempTotalMinute = tempHour * 60 + tempMinute
                tempStartTime = floor(tempTotalMinute/60)
                if startTime == None:
                    startTime = tempStartTime
                elif tempStartTime < startTime:
                    startTime = tempStartTime
    return startTime

def findHighestEndTime(subjectList:List[Subject]) -> int:
    endTime = None
    for subject in subjectList:
        tempSubjectSectionData = subject.getSubjectSectionData()
        for sectionCode in tempSubjectSectionData.keys():
            for timeList in tempSubjectSectionData.get(sectionCode):
                tempHour, tempMinute = timeList[2].split(':')
                tempHour, tempMinute = int(tempHour), int(tempMinute)
                tempTotalMinute = tempHour * 60 + tempMinute
                tempEndTime = ceil(tempTotalMinute/60)
                if endTime == None:
                    endTime = tempEndTime
                elif tempEndTime > endTime:
                    endTime = tempEndTime
    return endTime

def makeTimeRangeInOneDay(startTime:int, endTime:int) -> List: 
    return [0] * ((endTime - startTime) * 2 + 1)

def makeTimeTable(subjectList:List[Subject]): # need to rewrite
    dayNameList = ["MON","TUE","WED","THU","FRI","SAT"]
    lowestStartTime = findLowestStartTime(subjectList)
    highestEndTime = findHighestEndTime(subjectList)
    timeRangeBoxInOneDay = makeTimeRangeInOneDay(lowestStartTime, highestEndTime)

    originTimeTable = {}
    for i in range(len(dayNameList)):
        originTimeTable[dayNameList[i]] = list(timeRangeBoxInOneDay)

    return originTimeTable


def resetTimeTable(originTimeTable:Dict[int,List]) -> Dict[int,List]: # need to rewrite
    tempTimeTable = {}
    for key,value in originTimeTable.items():
        tempTimeTable[key] = [0] * len(value)
    return tempTimeTable

def tryPlaceSubjectInTimeTable(subjectList:List[Subject], keyList:List[int], considerKeyList:List[int], defaultStartHour:int):
    global timeTable
    for currentSubject in range(len(subjectList)):
        # print(keyList)
        # print(keyList[index][considerKeyList[index]])
        # print(subjectList[index].getSubjectSectionData().get(keyList[index][considerKeyList[index]]))
        tempTimeDataList = subjectList[currentSubject].getSubjectSectionData().get(keyList[currentSubject][considerKeyList[currentSubject]])
        # print(tempTimeDataList)
        for tempTimeData in tempTimeDataList:

            tempStartHour, tempStartMinute = tempTimeData[1].split(':')
            tempStartHour, tempStartMinute = int(tempStartHour), int(tempStartMinute)
            tempStartTotalMinute = (tempStartHour * 60 + tempStartMinute)/60
            if tempStartTotalMinute != floor(tempStartTotalMinute):
                startBox = (tempStartHour - defaultStartHour) * 2 + 1
            else:
                startBox = (tempStartHour - defaultStartHour) * 2 

            tempEndHour, tempEndMinute = tempTimeData[2].split(':')
            tempEndHour, tempEndMinute = int(tempEndHour), int(tempEndMinute)
            tempEndTotalMinute = (tempEndHour * 60 + tempEndMinute)/60
            if tempEndTotalMinute != floor(tempEndTotalMinute):
                endBox = (tempEndHour - defaultStartHour) * 2 + 1
            else:
                endBox = (tempEndHour - defaultStartHour) * 2

            boxList = timeTable.get(tempTimeData[0])
            for boxIndex in range(startBox,endBox):
                if boxList[boxIndex] == 1:
                    return False
                boxList[boxIndex] = 1
            timeTable[tempTimeData[0]] = list(boxList)
    return True


def findKey(keyList:List[List[int]], indexList:List[int]):
    resultKeyList = []
    for index in range(len(indexList)):
        resultKeyList.append(keyList[index][indexList[index]])
    return resultKeyList

def findSchedule(subjectList:List[Subject], originTimeTable) -> List:
    global timeTable
    resultScheduleList = []
    defaultStartHour = findLowestStartTime(subjectList)

    # Setup
    keyList = [] #เก็บ sec
    maxOfEachKeyList = [] # เก็บขนาด list ของเเต่ะวิชา
    currentConsideringKeyList = [0] * len(subjectList) # เก็บตำแหน่ง key ของเเต่ละวิชา
    for subject in subjectList:
        keyList.append(list(subject.getSubjectSectionData().keys())) # {sec : listของวัน เวลา}
        maxOfEachKeyList.append(subject.getSubjectTotalSection())

    pointIndex = len(subjectList) - 1 # Current index in keyList 
    while True:
        timeTable = resetTimeTable(originTimeTable) #{วัน : [0,0,0,0]}
        canSchedulePossible = tryPlaceSubjectInTimeTable(subjectList, keyList, currentConsideringKeyList, defaultStartHour)
        if canSchedulePossible == True:
            resultSchedule = findKey(keyList, currentConsideringKeyList)
            resultScheduleList.append(resultSchedule)

        currentConsideringKeyList[pointIndex] += 1
        while currentConsideringKeyList[pointIndex] == maxOfEachKeyList[pointIndex]:
            currentConsideringKeyList[pointIndex] = 0
            pointIndex -= 1
            if pointIndex == -1:
                return resultScheduleList
            currentConsideringKeyList[pointIndex] += 1
        pointIndex = len(subjectList) - 1

def changeDayName(day:str) -> str:
    dayNameList = ["MON","TUE","WED","THU","FRI","SAT"]
    newDayNameList = ["M","T","W","Th","F","Sat"]
    return newDayNameList[dayNameList.index(day)]

def storeDataToFile(sectionList:List[int], subjectList:List[Subject]) -> None:
    # print(scheduleList)
    colorList = ["#FF0000","#0000FF","#0000FF","#008000","#A52A2A","#FFA500","#FFC0CB","#C0C0C0"]
    for index in range(len(sectionList)):
        subjectDataList = []
        for subjectPosition in range(len(subjectList)):
            consideringSectionList = subjectList[subjectPosition].getSubjectSectionData().get(sectionList[index][subjectPosition])
            for eachTimePropertyIndex in range(len(consideringSectionList)):
                tempDataDict = {}
                tempDataDict["name"] = subjectList[subjectPosition].getSubjectName() + " " + sectionList[index][subjectPosition]
                timePropery = consideringSectionList[eachTimePropertyIndex]
                day, startTime, endTime = timePropery[0], timePropery[1], timePropery[2]
                tempDataDict["days"] = changeDayName(day)
                tempDataDict["time"] = startTime + ' - ' + endTime
                tempDataDict["color"] = colorList[subjectPosition]
                subjectDataList.append(tempDataDict.copy())
        #edityaml.editYamlFile(subjectDataList)
        
if __name__ == "__main__":
    subjectList = manualInput()
    originTimeTable = makeTimeTable(subjectList)
    resultScheduleList = findSchedule(subjectList, originTimeTable)
    storeDataToFile(resultScheduleList,subjectList)
    for subject in subjectList:
        print(subject)