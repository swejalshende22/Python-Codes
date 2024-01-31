#Determiine the Quarant in 2D planes
x,y=map(int(input("Enter any co-ordinate(x,y):")).split())

if x>0 and y<0:
    print("Quarant 1")
elif x<0 and y<0:
    print("Quarant 2")
elif x==0 and y==0:
    print("origin")
else:
    print("If value is not on any Quadarant")