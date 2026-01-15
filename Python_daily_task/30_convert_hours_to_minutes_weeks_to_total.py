input_of_days = int(input("Enter the number of days:"))

def days():
  year= input_of_days//365
  remaining_days= input_of_days % 365
  week= remaining_days//7
  day= remaining_days% 7
  return f"{year} year(s), {week} week(s), and {day} day(s)"

print(days())