def dictmarksrollno():
    d={}
    n=int(input("ENTER NO. OF STUDENTS YOU WOULD LIKE TO ADD"))
    for i in range(0,n):
        r=int(input("ENTER ROLL NUMBER"))
        m=int(input('ENTER MARKS OF STUDENT'))
        d[r]=m
    b=int(input("ENTER ROLL NO. OF STUDENT WHOM MARKS YOU WANT"))   
    print("MARKS OF ROLL NO",b,'IS',d[b])
dictmarksrollno()
