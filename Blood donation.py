age=int(input("Enter your Age:"))
gender=input("Enter your gender:")
weight=int(input("Enter your weight:"))

deasease=input("Enter your deases:") 

if age>=18:
    if gender=="male":

        if weight>=60:
            if deasease!="sugar":
                print("your eligible")
            else:
                print("sorry you are not eligible.")
    elif gender=="female":
            if weight>=45:
                if deasease!="sugar":
                    print("your eligible")
                else:
                    print("sorry you are not eligible.")
            
        