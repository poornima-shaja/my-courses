# #useing for loop 
pizzahut=["onion","corn","capsicum"]
for pizza in pizzahut:
    print(f"I love {pizza} so much")
print("\t\nThis defines that i love pizza so much\t\n")    

# #useing for loop
wild_animals=["tiger","lion","elephant"]
for wild in wild_animals:
    print(f"This is not a good idea to make a {wild} as a pet \n")

# #useing range 1 to 20
for twenty in range(1,21):
    print(twenty)

# #python will read everthing 1 to one million
for million in range(1,100):
    print(million)

# #max,min and sum with range
million = range(1,100001)
print(max(million))
print(min(million))
print(sum(million))

# #print 3 table 
for i in range(0,31,3):
    print(i)

# #print 3 table 3to90
threes=[]
for i in range(1,30):
    three=i*3
    threes.append(three)
print(threes)    

# #cubes 
cube_10=[]
for i in range(1,10):
    cube_10.append(i**3)
print(cube_10)    

# #squares comprehensions
squares =[value**2 for value in range(1,11)]
print(squares)
#cubes comprehensions
cube_10=[i**3 for i in range(1,11)]
print(cube_10)

# #slicing method
pizzahut_wild_animals=["onion","capsicum","tiger","lion","elephant"]
print(f"First three items are{(pizzahut_wild_animals[0:3])}")
print(f"Middle three items are{(pizzahut_wild_animals[1:4])}")
print(f"Last three items are{(pizzahut_wild_animals[2:])}")

# #copying a list 
my_fav=["jk","jimin","jhope","yoongi","jin"]
#display in seperate list
friend_fav=my_fav[:]
#display in same list
friend_fav=my_fav
my_fav.append("nanjoon")
friend_fav.append("tae")
print(my_fav)
print(friend_fav)



#tuples
food=("ice","coffee","chocolate","juice","cake")
for my_food in food:
    print(my_food)

print(type(food))

# food.append("banana")
# print(food)
