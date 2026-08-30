def counttype():
    s=input("enter somthing that you would like to check")
    v=0
    c=0
    n=0
    spc=0
    l=[]
    for i in s:
        if i not in l:
            if i in 'AEIOUaeiou':
                v=v+1
            elif i.isalpha():
                c=c+1
            elif i.isdigit():
                n=n+1
            else:
                spc=spc+1
        l.append(i)        
    print("NO. OF VOWELS ARE",v)
    print("NO. OF CONSONANTS ARE",c)
    print("NO. OF DIGITS ARE",n)
    print("NO. OF SPECIAL CHARECTERS ARE",spc)
counttype()


    
