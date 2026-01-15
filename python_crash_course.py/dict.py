#person
person={'first_name':"Park",
'last_name':"Jimin",
'age':27,
'city':'busan'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#favourite number
fav_num={
    'namjoon':1,
    'jin':2,
    'yoongi':3,
    'jhope':4,
    'jimin':5,
    'taehyung':6,
    'jungkook':7,
    }
print(f"jimin favourite num is {fav_num['jimin']}")    

#glosary1 and 2
gloss={
     'f-string':"to print the variable ",
     'loop':"to itrative any variable",
     'statment':"to add condiion ",
     'tuples':"these is immutable",
     'list': "list is mutable",
     'string': "these is immutable",
}
print(gloss)

for word,meaning in gloss.items():
    print(f"\n word:{word}")
    print(f"meaning:{meaning}")
 
for i in set(gloss.values()):
    print(i)    

#rivers
river={'nile':"egypt",
'ganga':"india",
'yellow river':"china",
}
for riv,ver in river.items():
    print(f"The {riv} runs through {ver}")

print("\nThe following rivers are: ")
for riv in river.keys():
    print(riv)    

print("\nThe following country are: ")
for riv in river.values():
    print(riv)

#Polling
fav_lang={
'poorni':"python",
'jimin':'djnago',
'jungkook':"java",
'jin':"c#",
'taehyung':"javascript",

}

players=['poorni','jimin','jhope','namjoion','jungkook','taehyung','jin','yoongi',]
for player in players:
    if player in fav_lang:
        print(f"\nThank you {player} for taking the poll")
    else:
        print(f"\nInviting {player} for taking a poll")    