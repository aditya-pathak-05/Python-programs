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
listevenoddseperate()
