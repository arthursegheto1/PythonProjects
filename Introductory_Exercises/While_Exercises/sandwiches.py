sandwich_orders =  ['chicken sandwich', 'egg sandwich', 'seafood sandwich',
                    'roast beef sandwich', 'grilled cheese', 'ham sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nI made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())