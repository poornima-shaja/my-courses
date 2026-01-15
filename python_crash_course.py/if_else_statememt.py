#chapter5 aliean color1
alien_color=input("enter your favourite color: ")
if alien_color == 'green':
    print("you earned 5 points")
if alien_color == 'red':
    print("you earned 0 points")
if alien_color == 'yellow':
    print("you earned 15 points ")
if alien_color == 'purple':
    print("you earned 1000 points ")
if alien_color in 'black':
    print(None)          

#alien color2
if alien_color == 'green':
    print("you got 5 points")
else:
    print("you got 10 points")    


#alien color3
if alien_color =='green':
    earned=5
elif alien_color =='yellow':
    earned=10
elif alien_color =='red':
    earned=15     
else:
    earned=None       
print(f"You earned for this game is {earned}")    

#Stages of life 
age=int(input("Tell me your age ? I'll tell you in which stage your in!!: "))
if age<=2:
    print("Your are a Baby")
elif age<=4:
    print("Your are a Toddler")
elif age<=13:
    print("Your are a Kid")
elif age<=20:
    print("Your are a teenager")
elif age<=65:
    print("Your are a adult")                
else:
    print("you are older")    

#fruits
fav_fruits=['banana','grapes','apple']
if 'banana' in fav_fruits:
    print("You really like banana")
if 'apple' in fav_fruits:
    print("You really like apple")
if 'grapes' in fav_fruits:
    print("You really like grapes")
if 'pine' in fav_fruits:
    print("You really like pine")            
if 'strawberry' in fav_fruits:
    print("You really like strawberry")    
    
