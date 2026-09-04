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
listswap()
