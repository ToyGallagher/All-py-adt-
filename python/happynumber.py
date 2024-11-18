'''while True:
        n = sumofsquare(19)
        if n ==1:
            print( True)
        else:
            sumofsquare(n)
        
        
def sumofsquare(self,n:int) -> int:
        output = 0
        while n:
            digit = n%10
            digit = digit**2
            output+=digit
            n=n//10
        return output'''

x = ["a","b","c"]
print(x.pop())