kilo_enter= int(input("Enter the distance in kilometres: "))
def convert_to_miles():
  miles= kilo_enter * 0.621371
  return miles

print(convert_to_miles())