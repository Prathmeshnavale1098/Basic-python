#Wap to check Enter number is multiple 7 and 3 using short hand if else
'''n= int(input("enter no to check  "))
print("It is multiple of 3 & 7") if n%3==0 and n%7==0 else print("It is not multiple of 3 & 7")'''

#Wap to print first n natural numbers in depending order get n from user
'''a = int(input("Enter a number:"))
while a>0 :
    print(a,end=" ")
    a-=1'''

#Wap to print 2s table in following format 2×1=2
'''num = 1
while num<=10:
    print("2 *",num,"=",2*num)
   #print(f"2*{num}= {2*num}")
    num+=1'''

#Wap to print even natural numbers upto 100
'''n= 2
while n<=100:
    print(n)
    n+=2'''

#Wap print addition of 1st n natural numbers
'''n=int(input("Enter a number:"))
sum = 0
while n>=1:
    sum=sum+n
   # print("Addition is:",sum)
    n-=1
print("Natueral number Addition is:",sum)'''

#Wap print addition of even number upto n natural numbers
'''num=int(input("Entered a number is:"))
sum = 0
while num>=1:
    if num%2==0:
        sum=sum+num
    num-=1
print("Addition of Even numbers is:",sum)'''

#Wap to print A to Z
'''ch=65
while ch<=90:
    print(chr(ch),end=" ")
    ch+=1'''

#Wap to display all number which are divisible by 13 but not by 3 between 100 to 500
'''n=100
while n<=500:
    if n%13==0 and n%3!=0:
        print(f"This is divisible by 13 and 3:{n}")
    n+=1'''
