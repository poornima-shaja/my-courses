#guest list
guest = ["jimin","park","mochi"]
print(f"{guest[0]} Inviting you for my birthday party")
print(f"{guest[1]} Inviting you for my birthday party")
print(f"{guest[2]} Inviting you for my birthday party")

#changing guest list
print(guest)
guest[1]= "filter"
print(guest)

#more guests
guest.insert(0,"poornima")
guest.insert(3,"nadar")
guest.insert(-1,"shanmuga")
print(guest)
#shrinking guest list
msg=("Only TWO people are invited in our dinner")
print(msg)

guest_not1= guest.pop()
print(f"Sorry cant invite you in dinner {guest_not1}")
guest_not2=guest.pop()
print(f"Sorry cant invite you in dinner {guest_not2}")

print(f"You're still inivited in dinner {guest[0]}")
print(f"You're still inivited in dinner {guest[1]}")
print(guest)

del guest[2]
print(guest)
del guest[2]
print(guest)

#length of the guest presen now in the list
len_guest=len(guest)
print(len_guest)






#organizing a list

world=["india","s.korea","london","fraance","germeny"]

#sorted list order
print(sorted(world))
#oringinal order
print(world)

#reverse the list
world.reverse()
print(world)
#original order
world.reverse()
print(world)

#sort it 
world.sort()
print(world)
#reverse sort it
world.sort(reverse=True)
print(world)
