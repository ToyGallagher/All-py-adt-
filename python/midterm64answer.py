text1 = 'Heavy Rotation'
text2 = 'I Love You'
length1 = len(text1)
length2 = len(text2)
textString1 = ''
textString2 = ''

for i in range(0,length2):
    for j in range(length2-i-1):
        textString2+=' '
    for j in range(0,i+1):
        textString2+=f'{text2[j]}'
    #for k in range(i-1,-1,-1):
        #textString2+=f'{text2[k]}'
    textString2+='\n'
    # print(f'1: {i}')
    '''
for i in range(1,length2):
    for j in range(i):
        textString2+=' '
    for m in range(0,length2-i-1):
        textString2+=f'{text2[m]}'
    for n in range(length2-i-1,-1,-1):
        textString2+=f'{text2[n]}'
    textString2+='\n'
    # print(f'2: {i}')

for i in range(0,length1):
    for j in range(length1-i-1):
        textString1+=' '
        # print(' ',end = '')
    for j in range(0,i+1):
        textString1+=f'{text1[j]}'
        # print(text1[j],end = '')
    for k in range(i-1,-1,-1):
        textString1+=f'{text1[k]}'
        # print(text1[k],end = '')
    textString1+='\n'
    # print(f'3: {i}')
    # print()

for i in range(1,length1):
    for j in range(i):
        textString1+=' '
        # print(' ',end = '')
    for m in range(0,length1-i-1):
        textString1+=f'{text1[m]}'
        # print(text1[m],end = '')
    for n in range(length1-i-1,-1,-1):
        textString1+=f'{text1[n]}'
        # print(text1[n],end = '')
    # if i == length1-1:
    #     textString1+=''
    # else:
    #     textString1+='\n'
    textString1+='\n'
    # print(f'4: {i}')
    # print()
'''
print(textString1+textString2)