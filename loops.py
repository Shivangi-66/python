n=float(input("enter the number:-"))
if n>4:
    result='A'
elif n>3:
    result='B'
elif n>2:
    result='C'
elif n>1:
    result='d'
print("grade is-", result)

# nested loops
list=["london","paris","berlin"]
for each in list:
    str1=each
    for s in str1:
        if(s=='o'):
            break
        print(s)
    print("\n")

for a in range(4):
    print("Hello World")