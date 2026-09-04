def countcase():
    s=input('ENTER A STRING')
    u=0
    l=0
    d=0
    lst=[]
    for i in s:
        if i not in lst:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            else:
                d+=1
        lst.append(i)        
    print("NO. OF UPPER CASE IS",u)
    print("NO. OF LOWER CASE IS",l) 
    print("NO. OF DIGIT/SPECIAL CHARACTER IS",d)
countcase()
