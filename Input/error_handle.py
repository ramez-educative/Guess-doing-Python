number = None
while number == None:
    try:
        n = input("Enter an integer: ")
        number = int(n)
    except Exception:
        print("Try again!")
print("Your number is", number)