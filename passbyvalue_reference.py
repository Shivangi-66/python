print("Pass by reference")
def pass_ref(list1):
    list1.extend([52,65])
    print("List inside the fuction:",list1)
list1=[12,74,96]
print("List before pass",list1)
pass_ref(list1)
print("List outside the function",list1)

print("\nPass by value")
def func(a):
    a=a+4
    print("Inside the function",a)
a=10
func(a)
print("Outside the function",a)