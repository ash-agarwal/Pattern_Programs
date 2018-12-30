for i in range(13):
    for j in range(19):
        if j>=i+7 and j<=11-i:
            print(" ",end="")
        elif j<=1-i or j>=17+i:
            print(" ",end="")
        elif i>3:
            if j>=i-3 and not j>21-i:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print("*",end="")
    print()
