#operators
car='subraru'
print("is car =='subraru' ?i think true")
print(car =='subraru' )

print("\nis car =='saufi' ?i think true")
print(car =='audi' )

bts='kim nanjoon'
print("Is bts=='kim nanjoon' is leader? i think true ")
print(bts=='kim nanjoon')
print(bts=='kim seokjin')


bias=['jimin', 'jin','jhope','namjoon','tae']
for bts in bias:
    if bts == 'jimin':
        print(bts.upper())
    else:
        print(bts.title())    


subjects=['ITSM','SQA','GIS','SCI','BI']  
for subject in subjects:
    if subject=='ITSM':
        print(subject.lower())
    else:
        print(subject.upper())    


age_0 = 22
age_1 =22
age_0 >= 21 and age_1 >= 21

age=19
age < 21