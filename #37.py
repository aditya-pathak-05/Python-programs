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
dictmarksmodify()
