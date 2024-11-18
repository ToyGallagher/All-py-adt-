
#def findTheDifference(s,t):
'''
s="abcd"
t="abcde"
sc=Counter(s)
tc=Counter(t)
for char,num in tc:
    if char not in sc or num!=sc[char]:
        print(char)
'''
#findTheDifference("abcd","abcde")
#Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

  
# Printing all the items of the Dictionary
#print(Dictionary1.items())

import collections
from collections import Counter
a_list = [1,2,3,4]
c_list = Counter(a_list)
print (c_list)

