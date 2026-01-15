user_entry = int(input("Enter the value: "))

def divisible():
    if user_entry %3==0 and user_entry %5==0:
        print("This number is divisible by both 3 and 5")
    elif user_entry %3==0:
        print("This number is divisible by only 3")
    elif user_entry %5==0:
        print("This number is divisible by only 5")
    else:
        print("Not divisible by 3 or 5")
divisible()
