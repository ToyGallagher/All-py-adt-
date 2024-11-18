def recursive_list_sum(data_list):
    total=0
    for i in data_list:
        if type(i) == type([]):  #เช็คว่าเป็น list ไหม
            total+=recursive_list_sum(i)
        else:
            total+=i
    return total
print(recursive_list_sum([2,4,[6,8],[10,12]]))