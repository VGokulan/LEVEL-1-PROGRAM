#!/usr/bin/env python
# coding: utf-8

# 1)Display “Hello World” in your output screen.


print("Hello World")


# 2)Get the input from the user and perform addition of two numbers


a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=a+b
print("Sum=",c)


# 3)swap two variables without temp variable


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=a+b
b=c-b
a=c-a
print("value of a=",a)
print("value of b=",b)


# 4)convert the entered kilometres ( Convertion  Factor= 0.621371)


km=int(input("Enter km value"))
m=km*0.621371
print("miles=",m)


# 5)check whether the given number is positive, negative or 0


a=int(input("Enter value:"))
if(a>0):
    print("It is positive value")
elif(a<0):
    print("It is negative value")
else:
    print("It is zero")


# 6)verify that the given year is a leap year


year=int(input("Enter year value:"))
if(year%400==0)&(a%100==0):
    print("It is a leap year")
elif(year%4==0)&(year%100!=0):
    print("It is leap year")
else:
    print("It is not a leap year")


# 7)display the prime numbers within the given interval


lower=int(input("Enter lower limit value: "))
upper=int(input("Enter upper limit value: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# 8) display the Fibonacci sequence up to n-th term


num=int(input("Enter value:"))
n1=0
n2=1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")


# 9) check if the number is an Armstrong number or not


a=int(input("Enter a number: "))
b=a//100
c=a%100
d=c//10
e=c%10
num=(b**c)+(d**3)+(e**3)
if num==a:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# 10) Find the Sum of natural numbers up to n-th term


a=int(input("Enter value: "))
s=0
if(a<=0):
    print("it is not a natural number")
else:
    for i in range(0,a+1):
        s=s+i
print(s)


# 11) Write a function called show_stars(rows). If rows are 5, it should print the following:
#  *
#  **
#  ***
#  ****
#  *****



row=int(input("Enter number of lines: "))
for i in range(1,row+1):
    print("*"*i)


# 12) Write a program to remove characters from a string starting from zero up to n and return a new string.


s=input("Enter any string: ")
n=int(input("Enter how much to remove:"))
b=len(s)
print(s[n:])


# 13) Iterate the given list of numbers and print only those numbers which are divisible by 5


l=[1,5,8,10,31,62,85,30,40]
for i in l:
    if i%5==0:
        print(i)


# 14) Write a program to find how many times substring “Hi” appears in the given string.


str=input("Enter the string :")
str2= 'hi'

count=str.count(str2)
print("Number of substring occurrences:",count)


# 15) Print the following pattern
#  1 
#  2 2 
#  3 3 3 
#  4 4 4 4 
#  5 5 5 5 5



row=int(input("Enter number of lines: "))
for i in range(1,row+1):
    print("% s" % i*i)


# 16) Write a program to check if the given number is a palindrome number.(A palindrome number is a number that is same after reverse. For example, 545, is the palindrome numbers)


pal=input("Enter a number")
if pal==pal[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")


# 17) Python program to interchange first and last elements in a list


l=[1,2,3,4,5]
print("Before interchanging:  ",l)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("After interchanging:  ",l)


# 18)Python program to swap two elements in a list


l=[1,2,3,4,5]
print("Before swapping: ",l)
x, y = int(input("Index one: ")), int(input("Index two: "))
l[x],l[y]=l[y],l[x]
print("After swapping: ",l)


# 19)Python | Ways to find length of list


l=[1,2,3,4,5]

#using built-in function
print("Length of list: ",len(l))

#using for loop
c=0
for i in l:
    c+=1
print("Length of list: ",c)


# 20)Maximum of two numbers in Python


a,b=int(input("enter value 1: ")), int(input("enter value 2: "))
if a>b:
    print("Maximum value is= ",a)
else:
    print("Maximum value is= ",b)


# 21)Minimum of two numbers in Python


a,b=int(input("enter value 1: ")), int(input("enter value 2: "))
if a>b:
    print("Minimum value is= ",b)
else:
    print("Minimum value is= ",a)


# 22)Python program to check whether the string is Symmetrical or Palindrome


val=input("Enter sting value: ")
print("pallindrome checking:\n")
if val==val[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
print("symmentrical checking:\n")
half=len(val)//2
if val[half:]==val[:half]:
    print("It is symmentrical")
else:
    print("It is not symmentrical")


# 23)Reverse words in a given String in Python


val=input("Enter sting value: ")
print(val[::-1])


# 24)Ways to remove i’th character from string in Python


s=input("Enter the string :")
i=int(input("Enter index  value: "))
s1=s[:i]+s[i+1:]
print(s1)


# 25)Find length of a string in python 

s=input("Enter the string :")

#using built-in function
print("Length of string: ",len(s))

#using for loop
c=0
for i in s:
    c+=1
print("Length of string: ",c)


# 26)Python program to print even length words in a string

n=input("Enter the string :")
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)

# 27)Python program to Find the size of a Tuple

t=(1,2,3,4,5)
print(len(t))

# 28)Python – Maximum and Minimum K elements in Tuple

t=(1,2,3,4,5)
print("Maximum value= ",max(t))
print("Minimum value= ",min(t))


# 29)Python – Sum of tuple elements

t=(1,2,3,4,5)
print("Sum of elements in the tuple:",sum(t))

# 30)Python – Row-wise element Addition in Tuple Matrix

tmat = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for row in tmat:
    s=sum(row)
    print("Row sum:",s)





