# Here I should write a function that should return a string formatted like this
# "Santiago, Chile"
# I should call at least 3 city-countries pairs and print the values returned.

def city_country(city_name, country):
    """Return a city-country pair name"""
    formatted_name = f"{city_name}, {country}"
    return formatted_name.title()

name_pairs = city_country('ouro branco', 'brazil')
print(name_pairs)

name_pairs = city_country('toronto', 'canada')
print(name_pairs)

name_pairs = city_country('geneva', 'switzerland')
print(name_pairs)