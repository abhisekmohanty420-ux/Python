try:
    
    a=int(input("Enter the First number:"))
    b=int(input("Enter the Second number:"))
    print(" What kind of operation do you want to perform.\n Press +for addition\n Press - for subtraction\n Press / for devision\n Press * for multiplication")
    o=input("Enter Operation")
    match o:
        case "+":
            print(f"the result is:{a+b}")
    match o:
        case "-":
            print(f"the result is:{a-b}")
    match o:
        case "*":
            print(f"the result is:{a*b}") 
    match o:
        case "/":
            print(f"the result is:{a/b}")                       
        
except Exception as e:
    print("perform valid opration")