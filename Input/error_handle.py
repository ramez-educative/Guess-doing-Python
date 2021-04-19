number = None
while number == None:
    n = input("Enter an integer: ")
    try:
        number = int(n)
    except Exception:
        print("Try again!")
print("Your number is", number)