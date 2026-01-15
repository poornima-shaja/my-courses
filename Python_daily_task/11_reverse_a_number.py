user = int(input("Enter the value: "))
user_str = str(user)
def reverse(user_str):
    result= user_str[::-1]
    return result 

print(reverse(user_str)) 