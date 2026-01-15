first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

def gcd(first, second):
  result=1
  for i in range(1, min(first, second)+1):
    if first % i==0 and second %i==0:
      result= i
  return result 

def lcm():
  return (first * second) // gcd(first, second)

print("The LCM is ", lcm())