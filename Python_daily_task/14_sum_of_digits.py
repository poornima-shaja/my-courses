user= int(input("Enter the value: "))
user_str = str(user)
def digit(user_str):
  total= 0
  for i in user_str:
    total+= int(i)
  return total 

print(digit(user_str))