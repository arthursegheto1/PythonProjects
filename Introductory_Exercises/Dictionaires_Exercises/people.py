person_0 = {'first_name': 'arthur', 'last_name': 'segheto', 'age': '19',
            'city' : 'ouro branco'}
person_1 = {'first_name': 'maria', 'last_name': 'morais', 'age': '19', 
            'city': 'ouro branco'}
person_2 = {'first_name': 'gustavo', 'last_name': 'segheto', 'age': '15', 
            'city': 'ouro branco'}

people = [person_0, person_1, person_2]

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")