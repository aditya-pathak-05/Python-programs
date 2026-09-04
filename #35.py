def nameno():
    ''' ENTERING DATA'''
    ln=[]
    lm=[]
    n=int(input("ENTER NO OF NAMES YOU WANT TO ADD"))
    for i in range(0,n):
        name=input("INPUT NAME")
        no=int(input("ENTER MOBILE NO."))
        ln.append(name)
        lm.append(no)
    ''' NOW GETTING ENTERED DATA'''
    a=input("ENTER NAME WHOSE PHONE NO. YOU WANT")
    for i in range(0,len(ln)):
        if ln[i]==a:
            b=i
    print('PHONE NO. OF',a,'IS',lm[b])
nameno()
