def binary_search(data,target,low,high):
    '''
    for i in data:
        if i == target:
            return True
    return False
            '''
    
    if low>high:
        return False
    else:
        mid =(low+high)//2
        if target == data[mid]:
            return True
        elif target< data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

data = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
print(binary_search(data,37,0,len(data)-1))
print(binary_search(data,22,0,len(data)-1))
print(binary_search(data,31,0,len(data)-1))
print(binary_search(data,13,0,len(data)-1))