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
    
 # 31)Create a list of tuples from given list having number and its cube in each tuple

l = [1,2,3,4,5]
p = [(i, pow(i, 3)) for i in l]
print(p)

# 32)Python | Sort Python Dictionaries by Key or Value

Dict = {'ram': 24, 'raj': 46,'ravi': 36, 'raja': 27, 'raju': 45}
K= list(Dict.keys())
K.sort()
sdict={i: Dict[i] for i in K}
print(sdict)

# 33)Python dictionary with keys having multiple inputs

d= {}
a,b,c= 5, 3, 10
p,q,r= 12, 6, 9
d["x-y+z"] = [a-b+c,p-q+r]
print(d)

# 34)Python program to find the sum of all items in a dictionary

d={'x':455,'y':223,'z':300,'p':908 }
print("Dictionary: ", d)
print("sum: ",sum(d.values()))

# 35)Python program to find the size of a Dictionary

dic1 = {"A": 1,"B": 2,"C": 3}
print("Size of dic1: ",len(dic1))

# 36)Find the size of a Set in Python

s={1,2,3,4,5}
print("Size of set: ",len(s))

# 37)Iterate over a set in Python

s=set("Hello_World")
for i in s:
    print(i)

# 38)Python – Maximum and Minimum in a Set

s={1,2,3,4,5}
print("Maximum of the set: ",max(s))
print("Minimum of the set: ",min(s))

# 39)Python – Remove items from Set

s={1,2,3,4,5}
print("Initial list: ",s)
s.remove(5)
print("Final list: ",s)

# 40)Python – Check if two lists have atleast one element common

s={1,2,3,4,5}
p={5,6,7,8,9}
for i in s:
    for j in p:
        if i==j:
            print("Element common is:", i)
# 41)Python – Assigning Subsequent Rows to Matrix first row elements

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("My matrix is:")

for i in range(1, len(matrix)):
    matrix[i] = matrix[0]

print(matrix)

# 42)Adding and Subtracting Matrices in Python

# Input matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
 

print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
 

print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
 

result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
 

print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()
 
# 43)Python – Group similar elements into Matrix

elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]


element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1


num_rows = max(element_counts.values())
num_cols = len(element_counts)


matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element


for row in matrix:
    print(row)
    
# 44)Python – Row-wise element Addition in Tuple Matrix

matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))


row_sums = [sum(row) for row in zip(*matrix)]


print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)
    
# 45)Create an n x n square matrix, where all the sub-matrix has the sum of opposite corner elements as even

def create_even_submatrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1

    return matrix


n = 4
result = create_even_submatrix(n)

for row in result:
    print(row)
    
 # 46)How to get list of parameters name from a function in Python?

import inspect

def my_function(guna,dinesh, kannan):
    pass

parameters = inspect.signature(my_function).parameters
parameter_names = list(parameters.keys())


print(parameter_names)

# 47)How to Print Multiple Arguments in Python?

def p(name, num):
    print("Hello from ", name + ', ' + num)
  
  
p("", "25")

# 48)Python program to find the power of a number using recursion

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)


base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

# 49)Sorting objects of user defined class in Python

class grade:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return str((self.a, self.b))
  

g= [grade("ram", 'a'),
       grade("ravi", 'b'),
       grade("raj", 'c'),
       grade("mani", 'd'),
       grade("goku", 's')]
  

print(sorted(g, key=lambda x: x.b))

# 50)Functions that accept variable length key value pair as arguments

def pk(**k):
    print(k)
 
if __name__ == "__main__":
    pk(w1='hello', w2='world')
