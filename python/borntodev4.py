password = {"ABd12341a":"Man", "123":"Non","We":"Miv"}
apb=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num=[0,1,2,3,4,5,6,7,8,9]
APH=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","r","S","T","U","V","W","X","Y","Z"]
new=[]
Man=[]
Non=[]
Miv=[]
for i in password:
    new.append(i)
print(new)
for j in new[0]:
    Man.append(j)
print(Man)
for k in new[1]:
    Non.append(k)
print(Non)
for l in new[2]:
    Miv.append(l)
print(Miv)


for Man in range(len(apb)):
    if Man in apb:
        xxx.append(Man)
        print("True")


'''
if password in Apb:
    if password in APH:
        if password in num:
            print(password)
'''