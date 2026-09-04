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
inputanddo()
