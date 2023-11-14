# Here, i'll add 'pastrami' in the list of the exercise "sandwiches"
# more than 3 times, to use 'remove'.

sandwich_orders =  ['chicken sandwich', 'egg sandwich', 'seafood sandwich',
                    'roast beef sandwich', 'grilled cheese', 'ham sandwich',
                    'pastrami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("\nWe've run out of pastrami, we're so sorry!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nI made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())