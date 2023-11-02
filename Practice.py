#Calculate the multiplication and sum of two numbers ()
#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum
'''num1 = 20

num2 = 30

print(num1*num2)

if(num1*num2)<1000:
    print(num1*num2)


else:
    print(num1+num2) '''
from typing import List

#Print sum of current no. and previous no.
"""num = 0

for i in range(1,11):
    sum = num + i
    print("current number",i , "previous number" , num , "sum" , sum)
    num = i """

#Write a program to accept a string from the user and display characters that are present at an even index number.
"""string = input("Enter a string")
size = len(string)
print(size)

for i in range(0,size - 1,2):
    print("index" , i  , string[i]) """

#Remove first 4 characters from string

"""name = "saffana"
print(name[4:]) """

#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
"""List = [1, 2, 3, 4, 5, 1]

print(List)
if List[0] == List[5]:
    print("True")
else:
    print("False")  """

#Iterate the given list of numbers and print only those numbers which are divisible by 5

"""num = [5,10,24,30,34,50]

for num in num:
    if num%5 == 0:
        print(num) """

#Return the count of a given substring from a string
#Write a program to find how many times substring “Emma” appears in the given string.

string = "Emma is good developer. Emma is a writer"
count = string.count("Emma")
print(count)

#Print the following pattern
"""1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 """

def function(n):
    for i in range(6):
      for j in range(i):
        print(i,end=" ")

print()

print("123")
print("abc")
