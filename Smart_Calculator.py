def Addition():
    num1=int(input("Enter value of num1:"))
    num2=int(input("Enter value of Num2:"))
    Add=num1+num2
    print("Addditon Result:", Add)

def Subtraction():
    num1=int(input("Enter value of num1:"))
    num2=int(input("Enter value of num2:"))
    sub=num1-num2
    print("Substraction Result:",sub)

def Division():
    num1=int(input("Enter value of num1:"))
    num2=int(input("Enetr value of num2:"))
    div=num1/num2
    print("Division Result:",div)

def Multiplication():
    num1=int(input("Enter value of num1:"))
    num2=int(input("Enter value of num2:"))
    mul=num1*num2
    print("Multiplication Result:",mul)

def Remainder():
    num1=int(input("Enter value of num1:"))
    num2=int(input("Enter value of num2"))
    result=num1%num2
    print("Remainder Result:",result)

def Exist():
    print("Thank you")



while True:
    print("1.Addition program")
    print("2.Sunstraction program")
    print("3.Division program")
    print("4.Multiplication program")
    print("5.Remainder program")
    print("6.Exist")
    
    choise=int(input("Enter your choise:"))
    if (choise==1):
        Addition()
    elif(choise==2):
        Subtraction()
    elif(choise==3):
        Division()
    elif(choise==4):
        Multiplication()
    elif(choise==5):
        Remainder()
    elif(choise==6):
        Exist()
        break

   
        
        
