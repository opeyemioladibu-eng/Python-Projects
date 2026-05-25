numbers = "1234567890"
special_char = "!@#$%^&*"
Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = "abcdefghijklmnopqrstuvwxyz"

while True:
    
    
    password = input("Enter Password:")
    
    
    if len(password)<8:
        print("Password must be at least 8 characters.")
        continue
    if not any(char in numbers for char in password):
        print("Password must contain a number.")
        continue
    if not any(char in special_char for char in password):
        print("password must contain a special character.")
        continue
    if not any(char in Uppercase for char in password):
        print("Password must contain an uppercase letter.")
        continue
    if not any(char in Lowercase for char in password):
        print("Password must contain a lower case letter.")
        continue

    print(f"{password} is a strong password.")
    break                
                

                
                
                
                
                
                
       