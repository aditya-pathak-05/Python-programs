def evenorodd():
    a=input('enter a no.')
    if a.isdigit():
        if int(a)%2==0:
            print("ENTERED NO. IS A EVEN NO.")
        else:
            print("ENTERED NO. IS A ODD NO.")
    else:
        print("ERROR: PLEASE ENTER A INTEGER")
evenorodd()        
