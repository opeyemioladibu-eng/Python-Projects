import random 
length = int(input("Password Length: "))
number = input('Include Number?[y/n]: ')
upper_case = input("Include uppercase?[y/n]:")
special_char = input("Include Special character?[y/n]:")


pool = "abcdefghijklmnopqrstuvwxyz" #base


if upper_case == 'y':
    pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if number == 'y':
    pool += "0123456789"
if special_char == 'y':
    pool += "!@#$%^&*"
    
    
password = ""
    
    
for i in range(length):
    password += random.choice(pool)


print(f"Suggested Password: {password}")