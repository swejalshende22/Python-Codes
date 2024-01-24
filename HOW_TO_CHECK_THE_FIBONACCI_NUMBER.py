#how to check the febonacci number
a=int(input("Enter any number:"))
x,y=0,1

#while loop
while y<a:
    x,y=y,x+y
if y==a:
    print("its a fibonacci number")
else:
    print("It is not fibonacci number")
    
    

 