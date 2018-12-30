for i in range(6):
    for j in range(i):
        if j==0:
            print("*",end="")
        elif i==5:
            print("*",end="")
        elif j==i-1:
            print("*",end="")
        else :
            print(" ",end="")
    print()
