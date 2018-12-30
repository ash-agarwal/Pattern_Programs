for i in range(10):
    for j in range(10):
        if i<5:
            if j<=i or j>=9-i:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if j<10-i or j>=i:
                print("*",end="")
            else:
                print(" ",end="")
    print()
