first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

def gcd(first, second):
  result=1
  for i in range(1, min(first, second)+1):
    if first % i==0 and second %i==0:
      result= i
  return result

print("The GCD is" , gcd(first, second))

# first = int(input("Enter the first number: "))
# second = int(input("Enter the second number: "))
# one_result= []
# two_result= []
# def gcd():
#     for i in range(1, first+1):
#         if i %2==0:
#             one_result.append(str(i))
#     for j in range(1, second+1):
#         if j %2==0:
#             two_result.append(str(j))
#     common = list(set(one_result) & set(two_result))
#     print(max(common))

# print(gcd())