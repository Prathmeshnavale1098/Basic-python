'''n=int(input("Enter a Number"))
s=0
t=0
while n>0:
    d=n%10
    s=s*10+d
    n//=10
print("Sum of digits",s)
if(s==t):
    print("Number os palindrone")
else:
    print("NUmber is not palindrone")'''

'''n=int(input("Enter a Number"))
s=0
t=n
while n>0:
    d=n%10
    s=s+d**3
    n//=10
print("Sum of digits",s)
if(s==t):
    print("Number is Amstronge")
else:
    print("NUmber is not Amstronge")'''

#WAP to take input from user and print n natural number in desending order using for loop
'''n=int(input("Enter a Number"))
for n in range(n,0,-1):
    print("Desending Order is:",n)'''

#WAP to print Febonacis series using for loop in python
'''n=int(input("Enter a number")) 
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,a+b'''

#WAP to check given number is prime or not
'''n=int(input("Enter a Number:"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if n>1 and flag==0:
    print("It is a Prime number")
else:
    print("It is not a prime number")'''

'''n=7
for i in range(2,n):
    print("It is not prime number")
    break
else:
    print("It is prime number")'''

'''Factorial Calculator with Input Validation .write a Python program that: 
1. Repeatedly asks the user to enter a non-negative integer. 
2. Use typecasting to convert the input to an integer. 
3. If the input is invalid or negative, print "Invalid input. Please enter a non-negative integer." and 
ask again. 
4. If valid, calculate and print the factorial of the number. 
5. After showing the factorial, ask the user if they want to calculate another factorial (yes or no). 
6. If the user enters "no", stop the program. If "yes", continue.'''

while True:
        n=int(input("Enter a non negative number:"))
        if n>=0:
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print("Factorial of",n,"is",fact)
        a=input("Do you want to calculate factorial(yes/no):")
        if a=="no":
            break
        if n<0:
            print("Invalid input.Please enter a non negative number.")