first_number = int(input("Enter the first value: ")) 
second_number = int(input("Enter the second value: ")) 
third_number = int(input("Enter the third value: "))

def greatest(): 
 if first_number > second_number and first_number > third_number:
  print(f" {first_number} is the greatest value") 
 elif second_number > first_number and second_number > third_number:
  print(f" {second_number} is the greatest value") 
 elif third_number > second_number and third_number > first_number:
  print(f" {third_number} is the greatest value")
 else:
  print("Two or more values are equal ")

greatest()