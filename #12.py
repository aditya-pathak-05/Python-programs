def solvequadratic():
    print("ASSUME QUADRATIC TO BE IN ax^2+bx+c FORM AND WRITE DOWN IT'S COEFICIENTS")
    a=int(input("ENTER COEF OF x^2"))
    b=int(input("ENTER COEF OF x "))
    c=int(input("ENTER THE CONSTANT TERM"))
    r1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
    r2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
    print("ROOTS OF THE GIVEN QUADRATIC EQN ARE",r1,'AND',r2)
solvequadratic()
