#1
def printmsg():
    print("HI HOW ARE YOU?")
#2    
def add():
    x=int(input("enter first no."))
    y=int(input("enter second no."))
    z=int(input("enter third no."))
    print("SUM OF ALL THREE NOS IS", x+y+z)
#3    
def measure():
    a=float(input("enter lenght of rect(in cms)"))
    b=float(input("enter breadth of rect(in cms)"))
    print("PERIMETER OF RECT IS", a+b,"cm")
    print("AREA OF RECT IS",a*b,"sq. cm")
 #4   
def result():
    n=input("enter name of student")
    a=float(input("enter marks in sub 1"))
    b=float(input("enter marks in sub 2"))
    c=float(input("enter marks in sub 3"))
    d=float(input("enter marks in sub 4"))
    e=float(input("enter marks in sub 5"))
    f=(a+b+c+d+e)/500*100
    print("TOTAL MARKS IS",a+b+c+d+e)
    print('PERCENTAGE OBTAINED',(a+b+c+d+e)/500*100)
    if f>=33:
        print('RESULT: PASS')
    else:
        print("RESULT: FAIL")        
#5    
def evenorodd():
    a=input('enter a no.')
    if a.isdigit():
        if int(a)%2==0:
            print("ENTERED NO. IS A EVEN NO.")
        else:
            print("ENTERED NO. IS A ODD NO.")
    else:
        print("ERROR: PLEASE ENTER A INTEGER")
#6        
def kmtomiles():
    x=input("enter kms")
    print(x,"kms in miles =", float(x)*0.621371,"miles")
#7    
def sum():
    a=int(input("enter no. of natural nos"))
    s=0
    for i in range(0,a):
        b=int(input("enter a no."))
        s=s+b
    print("sum is",s)
#8    
def printnnos():
    import random
    n=int(input("enter no of no.s u want "))
    s=int(input("enter a no. from where you want to start"))
    e=int(input("enter a no, from wher u want to end"))
    m=0
    l=[]
    while m<n:
        a=random.randint(s,e)
        if a not in l:
            l.append(a)
            m=m+1
        else:
            continue
    print("YOUR",n,"RANDOM NO'S ARE",l)
#9    
def sumofseries():
    x=int(input("enter a no"))
    n=int(input("enter its power"))
    s=0
    for i in range(0,n+1):
        a=x**i
        s=s+a
    print("SUM OF SERIES IS",s)
#10    
def ascorder():
    n=int(input("enter no. of no.s u want"))
    l=[]
    for i in range(0,n):
        a=int(input("enter a no"))
        if a not in l:
            l.append(a)
        else:
            print("ALREADY IN LIST ADD A DIFFERENT NO")
            l.append(int(input("enter a different no")))
        l.sort()     
    print("YOURS NO. IN ASC ORDER ARE",l)
#11
def determine():
    a=input("enter the thing that you want to determine")
    if a.isupper():
        print("IT'S A UPPER CHARACTER")
    elif a.islower():
        print("IT'S A LOWER CHARACTER ")
    elif a.isdigit():
        print("IT'S A DIGIT")
    else:
        print("IT'S A SPECIAL CHARACTER OR MIXED OF LOWER AND UPPER")
#12
def solvequadratic():
    print("ASSUME QUADRATIC TO BE IN ax^2+bx+c FORM AND WRITE DOWN IT'S COEFICIENTS")
    a=int(input("ENTER COEF OF x^2"))
    b=int(input("ENTER COEF OF x "))
    c=int(input("ENTER THE CONSTANT TERM"))
    r1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
    r2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
    print("ROOTS OF THE GIVEN QUADRATIC EQN ARE",r1,'AND',r2)
#13
def findfactorial():
    a=int(input("enter a no. for which you want to find factorial"))
    f=1
    for i in range(1,a+1):
        f=f*i
    print("FACTORIAL OF",a,'IS',f)
#14
def pattern1():
    for i in range(1,4):
        for j in range(1,4):
            print(i,end='')
        print()
#15
def pattern2():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end='')
        print()
#16
def pattern3():
    for i in range(5,1,-1):
        for j in range(1,i):
            print(j,end='')
        print()
#17
def pattern4():
    for i in range(1,5):
        for j in range(i,5):
            print(j,end='')
        print()
#18
def pattern5():
    for i in range(0,5):
        for j in range(4,i,-1):
            print(j,end='')
        print()
#19
def pattern6():
    for i in range(4,0,-1):
        for j in range(i,0,-1):
            print(j,end='')
        print()
#20
def pattern7():
    for i in range(4,0,-1):
        for j in range(i,0,-1):
            print(i,end='')
        print()
#21
def pattern8():
    for i in range(1,9,2):
        for j in range(1,i+1,2):
            print(j,end='')
        print()
#22
''' 1
    23
    456
    78910'''
    
    
#23
''' A
    BB
    CCC
    DDDD'''
#24
''' A
    AB
    ABC
    ABCD'''
#25
''' *
    **
    ***
    ****
    *****'''
#26
''' 1
    121
    12321
    1234321'''
#27
''' 4
    43
    432
    4321'''
#28
def counttype():
    s=input("enter somthing that you would like to check")
    v=0
    c=0
    n=0
    spc=0
    l=[]
    for i in s:
        if i not in l:
            if i in 'AEIOUaeiou':
                v=v+1
            elif i.isalpha():
                c=c+1
            elif i.isdigit():
                n=n+1
            else:
                spc=spc+1
        l.append(i)        
    print("NO. OF VOWELS ARE",v)
    print("NO. OF CONSONANTS ARE",c)
    print("NO. OF DIGITS ARE",n)
    print("NO. OF SPECIAL CHARECTERS ARE",spc)
#30
def reversestring():
    s=input("ENTER ANY STRING")
    for i in range(len(s)-1,-1,-1):
        print(s[i])
#31
def countcase():
    s=input('ENTER A STRING')
    u=0
    l=0
    d=0
    lst=[]
    for i in s:
        if i not in lst:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            else:
                d+=1
        lst.append(i)        
    print("NO. OF UPPER CASE IS",u)
    print("NO. OF LOWER CASE IS",l) 
    print("NO. OF DIGIT/SPECIAL CHARACTER IS",d)
#32
def lstchange():
    l=eval(input('ENTER A LIST'))
    a=input('DO YOU WANT TO DELETE ANY ELEMENT Y/N')
    while a.lower()=='y':
        d=int(input('select the index of element which you want to delete'))
        l.pop(d)
        a=input('DO YOU STILL WANT TO DELETE ANYTHING Y/N')
    b=input('DO YOU WANT TO INSERT ANYTHING Y/N')
    while b.lower()=='y':
        i=int(input('ENTER THE INDEX WHERE YOU WANT TO ADD'))
        e=int(input('ENTER THE ELEMENT THAT YOU WANT TO ADD'))
        l.insert(i,e)
        b=input('DO YOU STILL WANT TO ADD MORE ELEMENTS Y/N')
    print('YOUR FINAL LIST AFTER ALL CHANGES IS', l)
#33
def createandhigh():
    l=[]
    n=int(input("enter no. of elements you want in list"))
    for i in range(1,n+1):
        a=int(input("enter a no"))
        l.append(a)
    print('MAX NO. IS',max(l))
#34
def listswap():
    l=eval(input("ENTER A LIST"))
    if len(l)%2==0:
        for i in range(0,len(l),2):
            x=l[i]
            l[i]=l[i+1]
            l[i+1]=x
        print('SWAPPED LIST IS',l)
    elif len(l)%2!=0:
        for i in range(0,len(l)-1,2):
            x=l[i]
            l[i]=l[i+1]
            l[i+1]=x
        print('SWAPPED LIST IS',l)
#35
def nameno():
    ''' ENTERING DATA'''
    ln=[]
    lm=[]
    n=int(input("ENTER NO OF NAMES YOU WANT TO ADD"))
    for i in range(0,n):
        name=input("INPUT NAME")
        no=int(input("ENTER MOBILE NO."))
        ln.append(name)
        lm.append(no)
    ''' NOW GETTING ENTERED DATA'''
    a=input("ENTER NAME WHOSE PHONE NO. YOU WANT")
    for i in range(0,len(ln)):
        if ln[i]==a:
            b=i
    print('PHONE NO. OF',a,'IS',lm[b])
#36
def dictmarksrollno():
    d={}
    n=int(input("ENTER NO. OF STUDENTS YOU WOULD LIKE TO ADD"))
    for i in range(0,n):
        r=int(input("ENTER ROLL NUMBER"))
        m=int(input('ENTER MARKS OF STUDENT'))
        d[r]=m
    b=int(input("ENTER ROLL NO. OF STUDENT WHOM MARKS YOU WANT"))   
    print("MARKS OF ROLL NO",b,'IS',d[b])
#37
def dictmarksmodify():
    d={}
    n=int(input("ENTER NO. OF STUDENTS YOU WOULD LIKE TO ADD"))
    for i in range(0,n):
        r=int(input("ENTER ROLL NUMBER"))
        m=int(input('ENTER MARKS OF STUDENT'))
        d[r]=m
    a=input("DO YOU WANT TO MODIFY YOUR DICT Y/N")
    while a.lower()=='y':
        b=int(input("ENTER ROLL NO. OF STUDENT WHOM MARKS YOU WANT TO MODIFY"))   
        m=int(input("ENTER NEW MARKS"))
        d[b]=m
        a=input("DO YOU STILL WANT TO MODIFY Y/N")
    print('MODIFIED DICT IS',d)
#38
def inputanddo():
    n=int(input("ENTER A NO."))
    s=str(n)
    a=0
    c=0
    x=0
    for i in s:
        a=a+int(i)
        if int(i)%2==0:
            c=c+1
        x=x+1
    print('SUM OF DIGITS OF',n,'IS',a)
    print(n,'IN REVERSE ORDER IS',int(s[::-1]))
    print('NO. OF EVEN DIGITS ARE',c)
    print('TOTAL NO. OF DIGITS ARE',x)
#39
def listevenoddseperate():
    n=int(input("ENTER NO. OF NUMBERS YOU WANT TO ADD"))
    l=[]
    l1=[]
    l2=[]
    for i in range(0,n):
        a=int(input("ENTER A NUMBER"))
        l.append(a)
    for j in l:
        if j%2==0:
            l1.append(j)
        else:
            l2.append(j)
    print("LIST OF NO.S YOU ADDED IS",l)
    print("LIST OF ALL EVEN NO.S FROM ABOVE LIST IS",l1,'AND LIST OF ALL ODD NO.S FROM ABOVE LIST IS',l2)
