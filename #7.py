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
printnnos()    
