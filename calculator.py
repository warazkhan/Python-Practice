print("Welcome to your Calculator")
continueOperations = "Firstturn"
print("Your options are:")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit calculator")
selectedOption = int(input())

def Calculations():
    
    if selectedOption == 1:
        firstNumber = float(input("Add this: "))
        secondNumber = float(input("to this: "))
        print(str(firstNumber),"+",str(secondNumber),"=",str(firstNumber+secondNumber))
    
    elif selectedOption == 2:
        firstNumber = float(input("Subtract this: "))
        secondNumber = float(input("to this: "))
        print(str(firstNumber),"-",str(secondNumber),"=",str(firstNumber-secondNumber)) 
    
    elif selectedOption == 3:
        firstNumber = float(input("Multipy this: "))
        secondNumber = float(input("to this: "))
        print(str(firstNumber),"*",str(secondNumber),"=",str(firstNumber*secondNumber)) 
        
    elif selectedOption == 4:
        firstNumber = float(input("Divide this: "))
        secondNumber = float(input("by this: "))
        if secondNumber == 0:
            print("Second Number is 0, Result will be Infinite")
        else:
            print(str(firstNumber),"/",str(secondNumber),"=",str(firstNumber/secondNumber))
        
    elif selectedOption < 1 or selectedOption > 5:
        print("Invalid Syntax")
        

if __name__ == '__main__':
    
    
    while continueOperations == "Yes" or continueOperations == "Firstturn":
        
        if continueOperations == "Yes":
            print("Your options are:")
            print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit calculator")
            selectedOption = int(input())
            
        Calculations()
            
        if (continueOperations == "Yes" or continueOperations == "Firstturn" ) and selectedOption < 5:
            continueOperations = input("Do you want to continue using calculator(Yes/No): ")
        
        else:
            break
        
    print("Thank you for using the Calculator.")
