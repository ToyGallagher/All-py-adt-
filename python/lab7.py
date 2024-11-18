'''
def plus_matrix(A:List,B:List) -> List:
    result_matrix = []
    for i in range(len(A)):
        temp_row = []
        for j in range(len(A[i])):
            temp_row.append(A[i][j]+B[i][j])
        result_matrix.append(list(temp_row))
        temp_row.clear()
    return result_matrix

def print_matrix(A:List) -> None:
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}',end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(plus_matrix(A,B))
'''
#1
'''
def plus_matrix(a,b):
    c = []
    for i in range(len(a)): 
        row=[]
        for j in range(len(a[i])):
            row.append(a[i][j]+b[i][j])
        c.append(row)
    return c
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()
        
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(plus_matrix(A,B))
'''
#2
'''
def minus_matrix(a,b):
    c = []
    for i in range(len(a)): 
        row=[]
        for j in range(len(a[i])):
            row.append(a[i][j]-b[i][j])
        c.append(row)
    return c
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()
        
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(minus_matrix(A,B))
'''
#3
'''
def mul_const(A,c):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append((A[i][j])*c)
        result.append(row)
    return result

def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2
print_matrix(mul_const(A,c))
'''
#4
'''
def transpose_matrix(A):
    result = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        result.append(row)
    return result
 
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()
        
A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2
print_matrix(transpose_matrix(A))
'''
#5
'''
def mul_matrix(a,b):
    c = []
    for i in range(len(a)): 
        row=[]
        for j in range(len(b[i])):
            tempmul = 0
            for k in range(len(a[i])):
                tempmul+= a[i][k]*b[k][j]
            row.append(tempmul)
        c.append(row)
    return c
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()
        
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(mul_matrix(A,B))
'''
#6
'''
def mul_matrix(a,b):
    c = []
    for i in range(len(a)): 
        row=[]
        for j in range(len(b[i])):
            tempmul = 0
            for k in range(len(a[i])):
                tempmul+= a[i][k]*b[k][j]
            row.append(tempmul)
        c.append(row)
    return c
def power_matrix(A,c):
    result = []
    for i in range(1,c):
        if i == 1:
            result = mul_matrix(A,A)
        else:
            result = mul_matrix(result,A)
    return result
def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"{a[i][j]:^6}",end=' ')
        print()
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
print_matrix(power_matrix(A, c))
'''
