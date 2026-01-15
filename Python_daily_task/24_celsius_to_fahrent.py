user = int(input("Enter the value in temperature: "))

def convert_fahren():
  res = user * 9/5
  result = res + 32
  return "The Fahrenheit of the Celsius is:", result 

print(convert_fahren())