#1. Write a program to print "Hello World"

print("Hello World")



#2. Write a program to read int, float and sting type values from console and print values.
b = int(input("Enter an integer: "))
c = float(input("Enter a float: "))
d = input("Enter a string: ")

print("Integer:",b)
print("Float:", c)
print("String:", d)

#or
e=int(input("enter a number"))
print(type(e))
f=str(input("enter a name"))
print(type(f))
g=float(input("enter a float value"))
print(type(g)) 

   
#3. Write a Python program to purposefully raise Indentation Error and correct it.

a=int(input("enter a number= "))
if(a%2==0):
   print("the given number is even number")
else:
       print("the given number is odd number") #here i purposefully made a error that else: is the cureect one but i put only else
