list=['I','am','robo']
list1=[2,56,98,34]
print(list1[2])
print(list[:3])
print(list[:])
print(list[2:])
print(list1[1:3:1])
list[2]='abc'
print(list)
#print(delattr(list[2]))
print(list+list1)
print(list*2)
if 'an' in list:
    print("yes")
else:
    print('no')
print(max(list1))
print(sorted(list1))
