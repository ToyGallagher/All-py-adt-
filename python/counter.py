
'''import collections
from collections import Counter
#a_list = [1,2,2,3,4,4,4]
#c_list = Counter(a_list)
s = "abcd"
t = "abcde"
sc = Counter(s)
tc = Counter(t)
#print(tc)
for char,num in tc.items():
    #if char not in sc:
  print(sc[char])'''
  
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc=Counter(s)
        tc=Counter(t)
        for char,num in tc.items():
            if char not in sc or num !=sc[char]:
                return char'''

word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1
print(counter)