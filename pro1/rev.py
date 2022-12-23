#!/usr/bin/python3
def rev(str):
	str = str[ ::-1]
	return str
x = input("Enter the word to be reversed : ")
print ("The string in original form : ", x)
print ("The srting in reverse form : ", rev(x))

