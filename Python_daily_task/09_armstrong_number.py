user = int(input("Enter the value: ")) 
user_str = str(user)
user_len = len(user_str)
def armstrong():
  total = 0
  for i in user_str:
    total += int(i) ** user_len
  if total == user: 
    print("It's a Armstrong") 
  else: 
    print("It's not an armstrong")

armstrong()