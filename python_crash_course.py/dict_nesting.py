pets=[]
pet={
    'name':"bam",
    'breed':'toto',
    'owner':'jungkook',
    'color':'black'
}
pets.append(pet)
pet={
    'name':"yeontan",
    'breed':'baba',
    'owner':'teahyung',
    'color':'brow&grey'
}
pets.append(pet)

for pet in pets:
    print(f"here what i know about mentioned  {pet['owner']} dog") 
    for key,values in pet.items(): 
        print(f"{key} : {values}")