def main():
    receiver = str(input("Enter the receiver name : "))
    sender = str(input("Enter the sender's name : "))
    message = str(input("Enter message : "))
    print(write_letter(receiver, sender, message))


def write_letter(receiver, sender, message):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
         Dear {receiver},
         {message}
         {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
    
main()