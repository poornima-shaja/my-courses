#List
# number= [1,2,3,4,5]

number = input("Enter elements separated by space: ").split()
print("List:", number)
#using dict
#function
def unique(number):
  basket={}
  for i in number:
    if i in basket:
      basket[i]+=1
    else:
      basket[i]=1
  for key in basket:
    if basket[key]==1:
      return f"The odd man out of the given list is" ,key

print(unique(number))