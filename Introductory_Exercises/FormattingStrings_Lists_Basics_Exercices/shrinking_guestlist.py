name_list = ['Maria', 'João', 'Matheus']
print(name_list[0] + " would you like to have dinner at my house?")
print(name_list[1] + " would you like to have dinner at my house?")
print(name_list[2] + " would you like to have dinner at my house?")
print("I've found a bigger dinner table, now I have more guests to add to the list")
name_list.insert(0, 'Felipe')
name_list.insert(2, 'Pedro')
name_list.append('Gustavo')
print(name_list[0] + " would you like to have dinner at my house?")
print(name_list[1] + " would you like to have dinner at my house?")
print(name_list[2] + " would you like to have dinner at my house?")
print(name_list[3] + " would you like to have dinner at my house?")
print(name_list[4] + " would you like to have dinner at my house?")
print(name_list[5] + " would you like to have dinner at my house?")

print("\nOh no, the table won't arrive in time! I can invite only 2 people, sorry guys!")

pop_guests = name_list.pop()
print("\nSorry " + pop_guests + " I can't invite you because the table won't arrive in time, but I wait for you at the next party!")

pop_guests = name_list.pop()
print("\nSorry " + pop_guests + " I can't invite you because the table won't arrive in time, but I wait for you at the next party!")

pop_guests = name_list.pop()
print("\nSorry " + pop_guests + " I can't invite you because the table won't arrive in time, but I wait for you at the next party!")

pop_guests = name_list.pop()
print("\nSorry " + pop_guests + " I can't invite you because the table won't arrive in time, but I wait for you at the next party!")

print("\n" + name_list[0] + " I'm waiting for you at the party!")
print("\n" + name_list[1] + " I'm waiting for yout at the party!")

#These 2 lines are just to test the del method
#del name_list[0, 1]
#print(name_list)