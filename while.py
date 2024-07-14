# program to check the entered account number is correct or not
check_acc= 963852
num=int(input("Enter the account number-"))
while check_acc != num:
    print("Wrong account  number")
    num=int(input("Enter the right account number-"))
#print("\n")
print("Your account number is-", num)