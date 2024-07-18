class A():
    def sum(self,a,b):
        print("In Class A")
        c=a+b
        return c
class B(A):
    f=7
    def sum1(self,a,b):
        print("In Class B")
        c=a*a+b*b
        return c
b_obj=B()
print(B.__dict__)
print(b_obj.sum1(4,5))