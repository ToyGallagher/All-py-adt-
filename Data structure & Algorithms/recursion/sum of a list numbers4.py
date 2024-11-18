
def list_sum(num_list):
    '''
    # วิธีทั่วไป
    sum=0
    for i in num_list:
        sum+=i
    print(sum)
    '''

    # แบบ recursive
    if len(num_list)==1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
   
print(list_sum([3,6,9,12,16]))