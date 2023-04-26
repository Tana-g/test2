# T charecter
for i in range(7):
    for j in range(7):
        if j==3 or i==0 and j!=3 :
            print("*",end="")
        else:
            print(end=" ")
    n1=print()
print("\n")

#  A  charecter
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and (i!=0)) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    n2=print()
print("\n")

# N charecter
for i in range(6):
    for j in range(6):
        if (j==0 or j==5) or ((i==j and j>0 and j<5)):
            print("*",end="")
        else:
            print(end=" ")
    n3=print()
print("\n")

# A Charecter
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and (i!=0)) or ((i==0 or  i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    n4 = print()
