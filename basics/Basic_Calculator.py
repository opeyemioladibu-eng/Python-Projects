num = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
opp = input("Enter Operation[+,-,*,,/]:")
if opp =='+':
    print(num + num2)
elif opp == '-':
    print(num-num2)
elif opp == '*':
    print(num*num2)
elif opp == '/':
    print(num/num2)
else:
    print("invalid operation")