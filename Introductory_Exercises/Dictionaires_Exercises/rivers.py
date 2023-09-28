rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'mississippi': 'united states of america'
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

for river, country in rivers.items():
    print(f"\nRiver: {river.title()}")
    print(f"Country: {country.title()}")