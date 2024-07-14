ipl1=[]
ipl2=['r','c','b',18,'c',1,18 ]
ipl1.append("chennai")
ipl1.append("super")
ipl1.append("kings")
print(ipl1)

ipl1.extend(ipl2)
print(ipl1)
a='07'
ipl2.extend(a)
print(ipl2)

print(ipl2.count(18))
print(ipl2.index('c'))

ipl2.remove('c')
print(ipl2)

ipl1.pop(2)
print(ipl1)

ipl3=['m','t','y','c','x']
ipl3.sort()
print(ipl3)

ipl3.sort(reverse=True)
print(ipl3)

ipl2.reverse()
print(ipl2)

def func1(x):
    return x[1]
list_tup=[('s',5),('f',2),('z',9)]
list_tup.sort(key=func1)
print(list_tup)

#list comprehension
list=[2,5,9]
list1=[]
for i in list:
    list1.append(i*i)
print(list1)
[i*i for i in list] #this is list comprehension
print(list1)
[i*i for i in list if i%2==0]
print(list1)
