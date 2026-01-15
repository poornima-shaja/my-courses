first= int(input("Enter the first value: "))
second= int(input("Enter the second value: "))

def expo(first, second):
  result= first**second
  return result 

print(expo(first, second))


#without using **
base= int(input("Enter the base value: "))
exponent= int(input("Enter the exponent value: "))

def expo(base, exponent):
  result=1
  for i in range(exponent):
    result *= base
  return result 

print(expo(base , exponent))