# text = "aabbccddeeffg"
text = input("Enter elements separated by space: ")
print("List:", text)
def unique_string(text):
  basket={}
  for i in text:
    if i in basket:
      basket[i]+=1
    else:
      basket[i]= 1
#result show
  for key in basket:
    if basket[key] ==1:
      return f"The odd man out of the string is, {key}"

print(unique_string(text))