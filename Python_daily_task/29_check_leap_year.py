year= int(input("Enter the year:"))

def leap():
  if (year %4==0) and ((year%100!=0) or (year%400==0)):
    return "It's a leap year"
  else:
    return "It's not a leap year"

print(leap())