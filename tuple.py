tup1=(56,73,89,89.0,21)
tup2=(1,2,'hello','a')
print(tup2)
print(tup2[2])
print(tup2[:3])
a,b,c,d=tup2
print(d)

# tuple functions
print(len(tup2))
print(max(tup1)) # tup1 has 2 same values 89,89.0 but it will return the value that occurs first n the tuple
tup3=('az','rt','gh')
print(min(tup3))
print(tup1+tup3)
print(tup3*2)
print(id(tup3[2]))

"""built-in functions in string 
min,str(value--this converst the value into string)"""