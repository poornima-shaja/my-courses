user = int(input("Enter the value: "))
user_str = str(user)
def palindrome(user_str):
  result= user_str[::-1]
  if result== user_str:
    print(" It's a palindrome")
  else:
    print("It's not a palindrome")

palindrome(user_str)