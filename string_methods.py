str="This is me"
str1='1234'
print("The occurance of letter i is -" ,str.count("i") , "times")
print("Total number of letters in the given string is" , len(str))
print("find the word is in the sentence-", str.find("is"))
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.swapcase())
print(str.split())
list=str.split()
print(list[1])
print(str.ljust(13 ,'@'))
print(str.rjust(14 ,'#'))
print(str.center(18,'-'))
print(str.replace('me','pycharm'))
#print(str.join())
print(str.endswith('arm'))
print(str.isdigit())
print(str1.isdigit())
print(str.istitle())


