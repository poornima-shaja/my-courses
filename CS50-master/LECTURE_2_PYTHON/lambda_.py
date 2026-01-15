people=[
    {"name":"jin", "personality": "world wide handsome"},
    {"name":"rm", "personality": "IQ"},
    {"name":"jhope", "personality": "sunshine"},
    {"name":"jimin", "personality": "sweet"},
    {"name":"yooongi", "personality": "cat"},
    {"name":"jungkook", "personality": "banana milk"},
    {"name":"tae", "personality": "cute"},
]

people.sort(key=lambda person:person["name"])
print(people)