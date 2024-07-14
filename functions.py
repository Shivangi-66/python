"""
M- are identical functions in terms of name
M- are called on objects and passed on the data
F- it is called directly by name and passed on the data to operate
"""
def sum(a,b):
    c=a+b
    return c
x=10
y=20
print("sum of 2 numbers-" ,sum(x,y))

def info(name,age=20):
    print ("Name",name)
    print("Age",age)
info("shivi",age=22)
info("shruti")

def variable(var1,*vari):
    print("output is-",var1)
    for var in vari:
        print(var)
variable(60)
variable(100,20,60,90)