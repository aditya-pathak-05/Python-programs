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
    print("TOTAL MARKS IS",a+b+c)
    print('PERCENTAGE OBTAINED',(a+b+c)/300*100)
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
            

            
    
    
    
