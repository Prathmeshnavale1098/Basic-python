#WAP to print star traingle format
'''n=4
for i in range(1,4):
	print("*"*i)'''

'''for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''for i in range(4,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()'''

'''for i in range(1,5):
    for j in range(5,i,-1):
        print(i,end="")
    print()'''

'''for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

'''n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()'''

'''n='A'
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end="")
    print()
    n=chr(ord(n)+1)'''

'''n='A'
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end="")
        n=chr(ord(n)+1)
    print()'''
    
'''n='C'
for i in range(1,4):
    for j in range(4,i,-1):
        print(n,end="")
    print()
    n=chr(ord(n)-1)'''

'''n=4
for i in range(1,5):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()'''


'''for i in range(4,0,-1):
    for k in range(4-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()'''

'''rows = 4
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()'''
    
'''for i in range(1,5):
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(5,-1,-1):
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''

'''n=5
for i in range (1,n+1):
    for k in range (n-i):
        print(" ",end="")
    for j in range (2*i-1):
        print("*",end="")
    print()
    
'''n=5
for i in range (n,0,-1):
    for k in range (n-i):
        print(" ",end="")
    for j in range (2*i-1):
        print("*",end="")
    print()'''

'''n=4
ch=ord('A')
for i in range(1,n):
    for j in range(1,i+1):
        if (ch%2==0):
            print(chr(ch).lower(),end="")
            ch+=1
        else:
            print(chr(ch),end="")
            ch+=1
    print(6'''

'''for i in range(4):
    print("*")
print("*"*6)'''

'''n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
