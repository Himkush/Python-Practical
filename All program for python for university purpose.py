"""Python program for prime number"""

##a = int(input("Enter the range:"))
##for i in range(2,a):
##         flag = 0
##         for j in range(2,i):
##                  if(i%j==0):
##                           flag = 1
##                           break
##         if (flag == 0):
##                  print(i)
##                  

""""Python Program to print Fibonacci series"""

##num = int(input("Enter the range upto which you want"))
##a = 0
##b = 1
##c = 0
##print(a,"\n",b,sep="")
##for i in range(num):
##         c = a+b
##         print(c)
##         a = b
##         b = c
         
"""Demonstrating Fibonacci series using recursion """

##def fib(n):
##         f = 0
##         if n<=1:
##                  return n
##         else:
##                 return
##         fib(n-1)+fib(n-2)
##         
##num = int(input("Enter the range upto which you want"))
##for i in range(num):
##         print(fib(i))

""" ing wala """

##string = input("Enter a string:")
##if (string.endswith("ing"
##                    )):
##         string = string + "ly"
##else:
##         string = string + "ing"
##print(string)

""" $ wala """

##string = input("Enter a sentence:")
##temp = string[0]
##temp_string = string[0]
##for i in range(1,len(string)):
##         if string[i] == temp:
##                  temp_string += "$"
##         else:
##                  temp_string += string[i]
##                  
##print(temp_string)

"""To count frequency of word"""

##string = input("Enter a string")
##d ={}
##a  = string.split()
##for i in a:
##         d[i] = a.count(i)
##print(d)

"""To Take the string from the user and remove duplicates"""

##string = input("Enter a string:")
##b = string.split()
##b = list(set(b))
##b = sorted(b)
##temp = ""
##for i in b:
##         temp += i+" "
##print(temp)


""" To demonstrate queue"""

##from collections import deque
##
##a = deque([1,2,3])
##a.append(5)
##print(a)
##print(a.popleft())
##print(a.pop())
##print(a)

""" To demonstrate writing and reading from file"""
#use it before to create the file

##file = open("hello.txt","w+")
##file.write("Are Bhai Bhai Bhai Bhai")
##file.close()

# Aftercompletion of the program comment the above line

##file = open("hello.txt","r+")
##print(file.read(10))
##file.close()

##import shutil
##shutil.copy("Hello.txt","new.txt")



