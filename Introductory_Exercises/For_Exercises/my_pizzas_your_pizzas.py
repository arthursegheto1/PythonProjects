my_pizzas = ['calabresa', '4 Queijos', 'frango com catupiry']
friend_pizzas = my_pizzas[:]
print("My favorite pizzas are: ")
print(my_pizzas)
print("\nMy friend's favorite pizzas are: ")
print(friend_pizzas)

my_pizzas.append('lombo canadense')
friend_pizzas.append('marguerita')

print("\nMy favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title())
        