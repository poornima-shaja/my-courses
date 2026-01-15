a= int(input("Enter the first value: "))
b= int(input("Enter the second value: "))

def swap(a, b):
  a,b=b,a
  return a, b

a, b= swap(a,b)

print("The new first value is: " ,a)
print("The new second value is: " ,b)