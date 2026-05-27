import math
# Message to pop up upon start of program
def menu():
    print("\n ==== CALCULATOR ====")
    print("Press 0 to see Menu.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("9. View History")
    print("10. Clear History")
    print("11. Exit")    
    
menu()
    
    
#defining basic arithmetic function    
def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide (a, b):
    return a / b


#history list
history = []


#start of while(continuous) loop
while True:
    try:
        user_input = (input("\nEnter Operation[0/1/2/3/4/5/6/7/8/9/10/11]:"))
        
        
        if user_input not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            raise ValueError
        
        
        if user_input in ["5", "6", "7", "8"]:
            num1 = float(input("Enter Number: "))
            if user_input == "5":
                if num1< 0:
                    print("Cannot Square root a negative number.")
                else:
                    results = math.sqrt(num1)
                    print(f"Result: {results}")
                    history.append(f"Square root:{num1} = {results}")
            elif user_input == "6":
                results = math.sin(math.radians(num1))
                print(f"Result: {results}")
                history.append(f"Sine{num1} = {results}")
            elif user_input == "7":
                results = math.cos(math.radians(num1))
                print(f"Result: {results}")
                history.append(f"Cosine{num1} = {results}")
            elif user_input == "8":
                results = math.tan(math.radians(num1))
                print(f"Result: {results}")
                history.append (f"Tangent{num1} = {results}")
        
        
        
        
        if user_input in ['0', '1', '2', '3', '4', '9', '10', '11']:
            
        
            if user_input == "0":
                menu()
                continue # goes back to the loop
            elif user_input == "9":
                if not history:
                    print("No history yet.")
                else:
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                continue
            elif user_input == "10":
                history.clear()
                print("History cleared.")
                continue
            elif user_input == "11":
                print("Program Closed")
                break
            
            
            num1 = float(input("Enter First Number:"))
            num2 = float(input("Enter Second Number:"))           
            if user_input == "1":
                results = add(num1, num2)
                print(f"Result:{results}")
                history.append(f"{num1} + {num2} = {results}")
            elif user_input == "2":
                results = subtract(num1, num2)
                print(f"Result:{results}")
                history.append(f"{num1} - {num2} = {results}")
            elif user_input == "3":
                results = multiply(num1, num2)
                print(f"Result:{results}")
                history.append(f"{num1} * {num2} = {results}")
            elif user_input == "4":
                if num2 == 0:
                    raise ZeroDivisionError
                results = divide(num1, num2)
                print(f"Result:{results}")
        
            
    except ValueError:
        print("Enter Valid Number.")
        continue    
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    except Exception :
        print(f"Unexpected error: {Exception}")
        
        
        
