prompt = "\nWhat kind of pizza toppings would you like to add?"
prompt += "\n(Enter 'quit'  when you're done!)"

while True:
    pizza = input(prompt)
    
    if pizza == 'quit':
        break
    else:
        print("I'll add " + (pizza) + " to your pizza!")