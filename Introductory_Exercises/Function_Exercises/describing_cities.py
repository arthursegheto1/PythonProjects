# In this exercise, I should use a default parameter for the country
# I should call the function for 3 different cities, and at least one that
# isn't in the default country.
# The function should print a simple sentence.

def describe_city(name, country='Brazil'):
    """Display information about a city"""
    print(f"{name.title()} is in {country.title()}")

# Just a city in Brazil, using the default value of 'country'
describe_city('ouro branco')
describe_city('belo horizonte')

# A city that isn't using the default value of 'country'
describe_city(name='toronto', country='canada')