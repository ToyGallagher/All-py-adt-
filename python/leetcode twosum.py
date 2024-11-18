nums=[3,2,4]
target=6
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==target and i!=j:
          print(i,j)
    #for j in range(len(nums)):
        
            #if nums[i]+nums[j]+nums[k]==target and i!=j!=k:
                #print(nums[i],nums[j],nums[k])


