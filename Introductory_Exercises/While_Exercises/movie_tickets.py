prompt = "\nHow old are you?"
prompt += "\n(Please, enter 'quit' if you're done!)"

while True:
    age = input(prompt)

    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age >= 3 and age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")