one= int(input("Enter the first value: "))
two= int(input("Enter the second value: "))

def prime():
  for i in range(one, two+1):
    if i > 1:
        for j in range(2, i):
          if i % j ==0:
            break
        else: 
            print(i)
prime()