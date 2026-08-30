def findfactorial():
    a=int(input("enter a no. for which you want to find factorial"))
    f=1
    for i in range(1,a+1):
        f=f*i
    print("FACTORIAL OF",a,'IS',f)
findfactorial()
