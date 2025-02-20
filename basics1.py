QUESTIONS FROM - https://www.w3resource.com/python-exercises/python-basic-exercises.php

#Current DateTime Display
import datetime
x = datetime.datetime.now()
print(x)

#Circle Area Calculator
x = int(input("Enter Radius : "))
a = (x * x * 22)/7
print(a)

#Reverse Full Name
x = input("Enter String : ")
print(x[::-1])

#List and Tuple Generator
x = input("Enter Numbers (Comma seperated, e.g. 1,4,7) : ")
a = x.split(",")
b = tuple(a)
print(a)
print(b)

#File Extension Extractor
import os
filename = "haha.png"
root, ext = os.path.splitext(filename)
print("File Extension:", ext)

#Number Expansion Calculator
#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a = int(input("Input an integer: "))

n2 = int("%s%s" % (a, a))   
n3 = int("%s%s%s" % (a, a, a)) 
print(a+n2+n3)

#Monthly Calendar Display
import calendar

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

#Write a Python program to calculate the number of days between two dates.
from datetime import date

f_date = date(2025, 6, 3)
l_date = date(2026, 8, 10)

diff = l_date - f_date
print(diff.days)

#Write a Python program to get the volume of a sphere with radius six.
r = 6
a = (22/7) * (6**2) * 4
print(a)

#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
x = int(input("Enter number : "))
y = 17
if x<=17:
    print(y-x)
else:
    print(2*(x-y))

#Write a Python program to test whether a number is within 100 of 1000 or 2000.
x = int(input("Enter number : "))
if (x>=900 and x<=1100) or (x>=1800 and x<=2100):
    print("In range")
else:
    print("Out of range")

#Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
x1 = float(input("Enter number : "))
x2 = float(input("Enter number : "))
x3 = float(input("Enter number : "))

if x1==x2==x3:
    print(3*(x1+x2+x3))
else:
    print(x1+x2+x3)

#Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
x = input("Enter String : ")

if len(x) >= 2 and x[:2] == "is":
    print(x)
else:
    print("is" + x)

#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
x = input("Enter String : ")
c = int(input("Enter number of copies : "))
result = ""
for i in range(c):
    result = result + x
print(result)

#Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
x = int(input("Enter Number : "))
if x%2 == 0:
    print("Even")
else:
    print("Odd")

#Count 4 in List
x = input("Enter elements (Comma seperated) : ")
myList = x.split(",")
count = 0
for i in myList:
    if i == "4":
        count = count + 1
print(count)

#Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
x = input("Enter string : ")
c = int(input("Enter number of copies : "))

if len(x) >=2:
    print(c*x[:2])
else:
    print(c*x)

#Write a Python program to test whether a passed letter is a vowel or not.
x = input("Enter letter : ")
vList = ["a","e","i","o","u"]
if x in vList:
    print("Vowel")
else:
    print("Consonent")

#Write a Python program that checks whether a specified value is contained within a group of values.
x = int(input("Enter value : "))
vList = [1,20,45,4]
if x in vList:
    print("Present")
else:
    print("Not Present")

#Write a Python program to create a histogram from a given list of integers.
x = input("Enter value (Comma seperated): ")
vList = x.split(",")
fList = []
for i in vList:
    fList.append(int(i))

for i in fList:
    for j in range(i):
        print("@",end="")
    print("\n")

#Write a Python program that concatenates all elements in a list into a string and returns it.
x = input("Enter value (Comma seperated): ")
vList = x.split(",")
myStr = ""
for i in vList:
    myStr = myStr + i
print(myStr)

#Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
x = int(input("Enter Upper Range : "))
if x>237:
    for i in range (237,x):
        if i%2 == 0:
            print(i)
else:
    print("Please enter value higher than 237")

