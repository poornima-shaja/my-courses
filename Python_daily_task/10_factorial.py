user = int(input("Enter the value: "))
def fact():
  result= 1
  for i in range(1 , user + 1):
   result= result* i
  return result

print(fact())
