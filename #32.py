def lstchange():
    l=list(eval((input('ENTER A LIST'))))
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
lstchange()
