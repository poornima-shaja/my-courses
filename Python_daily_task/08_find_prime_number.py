user = int(input("Enter the value: ")) 
def prime(): 
 if user > 1: 
  for i in range(2, user):
   if user % i == 0: 
    print("It's not a prime number")
    break
  else: 
   print("It's a prime number") 
 else: 
  print("It's not a prime number")

prime()