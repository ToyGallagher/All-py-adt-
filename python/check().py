def solution(s):
     for i in range(len(s)):
       if s[i]=='(' and s[i+1] == ')':
           
              return True
       if s[i]=='[' and s[i+1] == ']':
            
              return True
       if s[i] =='{' and s[i+1] == '}' :
            
              return True
        
       else:
            return False

'''
        if s[i]=='(':
            if s[i+1] != ')':
              return False
        if s[i]=='[':
            if s[i+1] != ']':
              return False
        if s[i] =='{':
            if s[i+1] != '}':
              return False
        
        else:
            return True
     '''


s1="()"
s2="()[]{}"
#s3="{]"
s3 = "{[()]}"
s4="([)]"


print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
