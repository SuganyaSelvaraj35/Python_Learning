# String practice

str1 = "SuganyaSelvarajconsulting.com"
str2 = "Selvaraj"
age = 31
str3 = "  magizhiniyan  "

print(str1[0:7]) # printing substring in python

print(str2 in str1) # whether one string is present in other string

print("{}{}{}".format(str1, " age is ", age)) # different data type concatenation

split_result = str1.split("j")

print(split_result)

print(split_result[1]) # after split, 1st index element will be displayed

print(str3.strip()) # trim the extra spaces present in the entire string(left+right side)

print(str3.lstrip()) # trim the extra spaces present on the left side of the string

print(str3.rstrip()) # trim the extra spaces present on the right side of the string