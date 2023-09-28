pet_0 = {'name' : 'miucha', 'type' : 'dog', 'owner' : 'arthur'}
pet_1 = {'name' : 'lilica', 'type' : 'dog', 'owner' : 'maria'}
pet_2 = {'name' : 'lolita', 'type' : 'dog', 'owner' : 'maria'}
pet_3 = {'name' : 'luna', 'type' : 'cat', 'owner' : 'pedro'}
pet_4 = {'name' : 'luke', 'type' : 'cat', 'owner' : 'matheus'}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nName: {pet['name'].title()}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")