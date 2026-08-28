def result():
    n=input("enter name of student")
    a=float(input("enter marks in sub 1"))
    b=float(input("enter marks in sub 2"))
    c=float(input("enter marks in sub 3"))
    d=float(input("enter marks in sub 4"))
    e=float(input("enter marks in sub 5"))
    f=(a+b+c+d+e)/500*100
    print("TOTAL MARKS IS",a+b+c+d+e)
    print('PERCENTAGE OBTAINED',(a+b+c+d+e)/500*100)
    if f>=33:
        print('RESULT: PASS')
    else:
        print("RESULT: FAIL")
result()
