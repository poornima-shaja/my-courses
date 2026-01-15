hour= int(input("Enter the hours: "))

minutes= int(input("Enter the minutes: "))

def total_in_seconds(): 
  hours_total= hour*3600 
  minutes_total= minutes* 60 
  total = hours_total + minutes_total
  return 'The total number of seconds of the given data is: ' , total
print(total_in_seconds())