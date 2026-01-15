# #hello admin
users=[]
users=['admin','jimin','park','chimchim']
if users:
    for user in users:
        if user=='admin':
            print("welcome admin!! wanna see the report?")
    else:
        print(f"hello,{user} Thank you for logging in again")    
else:
    print("we need more users")


#checking username
curr_user=['admin','jimin','park','chimchim', 'jiminjams']
new_users=['admin','jimin','park','chim','tatamic']
current_users_lower = []
for user in curr_user:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.") 

#ordinaral number 
numbers=list(range(1,11))
for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")