# text = "I love programming"
text = input("Enter elements separated by space: ")
print("List:", text)
vowel = {"a", "e" ,"i","o", "u"}
def vowel_count(text):
  result=0
  for i in text:
    if i.lower() in vowel:
      result+=1
  return f"Total vowels in string is :{result}"

print(vowel_count(text))