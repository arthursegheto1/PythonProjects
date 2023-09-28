cities = {'ouro branco': {
    'country' : 'brazil',
    'population' : '40.000',
    'fact' : 'The city has the famous Serra de Ouro Branco',
},
    'toronto': {
    'country' : 'canada',
    'population' : '2.93 million',
    'fact' : 'The city is the capital of the province of Ontario',

    },
    'zurique': {
    'country' : 'switzerland',
    'population' : '402.275',
    'fact' : 'The city is the largest in Switzerland',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print(f"\nCity: {city.title()}")
    print(f"Country: {country}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")