'''t=(5,5,5,5)
s=set(t)
print(s)
if len(s)==1:
    print("Tuple are Same")
else:
    print("Tuples are not same")'''

#WAP to remove duplicate elements from given list and accept elements of a list from users.
'''n=int(input("Enter a number of elements:"))
l=[]
for i in range(n):
        x=int(input("Enter a element:"))
        l.append(x)
new_list=[]
for i in l:
    for i not in new_list:
        new_list.append(i)
print("List after removing duplicates:",new_list)'''
#l=[int(i)for i in input()split()]
'''L1=[]
for i in range(4):
    a=int(input(a))
    L1.append(a)
print("",set(L1))'''

#WAP to create dictionary for employees details
'''d={'Name':'abc','emp_id':'1234','emp_sal':'30000'}
print(d)
d['Name']='Sam'
print(d)
for i in d:
    print(i)
for (i,j) in d.items():
    print(i,j)
del d['Name']
print(d)'''
'''del d
print(d)'''

'''d=dict(a='One',b='two')
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get('a'))
print(d['a'])
d.popitem()
print(d)
print(d.pop('a'))
print(d)
d['a']='Two'
print(d)
d['a']='One'
print(d)
d.clear()
print(d)'''

'''s='Python is very easy Python is programming Language'
d={}
for i in s:
    d[i]=s.count(i)
print(d)'''

#Function with no parameter
'''def f1():
    return 10+20,2*3
print(f1())
a,b=f1()
print(f1())'''

#Function with Parameter
'''def f1(a,b):
    return(a**b)
print(f1(2,3))
a=f1(2,3)
print(a)'''

#Fuction with multiple arguments
'''def f1(*a):
    print(sum(a))
    #print(a[2])
f1(1,2,3)
f1(10,20,30,40)
f1(35)'''

#Function with positional arguments
'''def f1(x,y):
    print(x,y)
f1(y=10,x=20)
f1(10,20)'''

#Function with keyword argument
'''def f1(**kargs):
    print(kargs)
    print(len(kargs))
f1(x=10,y=30,z=20)
f1(a=1,b=2)
f1(n=100)'''

#call back values
'''def f1(x,y):
    print(x,y)
    x=100
    y=200
    print(x,y)
f1(10,20)
x=1
y=2
print(x,y)
x+=3
print(x,y)'''

'''def f1(x,y):
    x,y=y,x
x=10
y=20
f1(x,y)
print(x,y)'''

#Function with call by referance
'''def f1(l):
    l[0]=100
l=[1,2,3]
f1(l)
print(l)'''

#WAF that access a number and check wheter its perfect number or not
'''def perfect(s):
    sum=0
    for i in range(1,s):
        if s%i==0:
            sum+=i
    if sum==s:
        print("That is a perfect number:",s)
    else:
        print("That is not perfect number:",s)
s=int(input("Enter a number to check"))
perfect(s)'''

#WAP in which function accept list having even number of elements and swap elements at adjustent position
'''def f(l):
    for i in range(0,len(l),2):
        l[i],l[i+1]=l[i+1],l[i]
    print(l)
l=[1,2,3,4,5,6]
if (len(l)%2==0):
    f(l)
else:
    print("List don't have a even numbers")'''
