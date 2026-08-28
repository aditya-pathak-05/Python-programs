def determine():
    a=input("enter the thing that you want to determine")
    if a.isupper():
        print("IT'S A UPPER CHARACTER")
    elif a.islower():
        print("IT'S A LOWER CHARACTER ")
    elif a.isdigit():
        print("IT'S A DIGIT")
    else:
        print("IT'S A SPECIAL CHARACTER OR MIXED OF LOWER AND UPPER")
determine()        
