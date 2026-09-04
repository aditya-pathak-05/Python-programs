def createandhigh():
    l=[]
    n=int(input("enter no. of elements you want in list"))
    for i in range(1,n+1):
        a=int(input("enter a no"))
        l.append(a)
    print('MAX NO. IS',max(l))
createandhigh()
