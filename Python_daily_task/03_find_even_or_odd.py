number= int(input("Enter the number: "))
def value(number):
    if number % 2==0:
        print("This value is an Even Number")
    else:
        print("This value is an Odd Number")
    return number
print(value(number))