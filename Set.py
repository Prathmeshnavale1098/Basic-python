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
