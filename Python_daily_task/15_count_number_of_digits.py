user= int(input("Enter the value: "))
user_len = len(str(user))

def length():
  return user_len

print(length())






#without using len() or str()
user= int(input("Enter the value: "))

def number(num):
  counter=0
  while num > 0:
    counter+= 1
    num= num//10
  return counter
print(number(user))