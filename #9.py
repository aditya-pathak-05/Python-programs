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
ascorder()    
