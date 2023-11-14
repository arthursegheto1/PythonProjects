responses = {}
polling_active = True

while polling_active == True:
    name = input("\nWhat is your name? ")
    response = input("Tell me a place that you dream about visiting someday")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would go to {response}")