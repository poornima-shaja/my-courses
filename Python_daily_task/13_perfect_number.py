user= int(input("Enter the value: "))
def perfect(user):
  total = 0
  for i in range(1, user):
    if user % i == 0:
      total+= i
  if total==user:
    return "It's a perfect number"
  else:
    return "It's not a perfect number"
print(perfect(user))