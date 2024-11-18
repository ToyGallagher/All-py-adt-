def geomatric_sum(n):
    if n<0:
        return 0 
    else:
        return 1/(pow(2,n))+geomatric_sum(n-1)
print(geomatric_sum(9))
print(geomatric_sum(6))