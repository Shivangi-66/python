#WAP to take input string from user and print the length of string
str=input("Enter any string-")
print(f"Lenght of the string is- {len(str)}")

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
print (f"string is-{str[:2]+str[-2:]}")

"""Write a Python program to get a single string from two given strings by user , separated by a space and swap the
 first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'"""
a=input()
b=input()
m=b[:2]+a[2:]+" "+a[:2]+b[2:]
print(m)

"""Write a Python program to change a given string to a new string where all the even position characters are in 
starting and all odd position characters are in end."""
str="shivangi"
n=str[0::2]+" "+ str[1::2]
print(n)

#Write a Python program to remove the characters which have odd index values of a given string
str="python"
m=str[::2]
print(m)
#WAP to insert a string in the middle of a other string.
str="shubipatil"
divide=len(str)//2
m=str[:divide]+"tejas"+str[divide:]
print(m)