principal= int(input("Enter the value of principal: "))
rate= int(input("Enter the rate of interest: "))
time= int(input("Enter the time: "))

def simple_interest():
  res= principal* rate*time
  result= res/100
  return f"The simple interest is: {result}"


print(simple_interest())