game_list = ['The Last Of Us 1', 'The Last Of Us 2', 'Red Dead Redemption 1', 'Red Dead Redemption 2', 'Minecraft', 'Stardew Valley', 'The Witcher 3']
total = len(game_list)
print(total)
print(game_list)

#Using insert and append methods to add itens to the list.
print("\nAdding games to the list: ")
game_list.insert(0, 'Assassins Creed')
game_list.insert(5,'League Of Legends')
game_list.insert(6, 'Valorant')
game_list.append('Call Of Duty')


#Using pop method to remove itens from the list
pop_games = game_list.pop()
print("\nRemoving " + pop_games + " from the list: ")
print(game_list)
pop_games = game_list.pop(6)
print("\nRemoving " + pop_games + " from the list: ")
print(game_list)

#Using del method 
del game_list [5]
print(game_list)

#Using methods to manipulate the list structure and order
print("\nHere is the sorted list: ")
print(sorted(game_list))
print("\nHere is the original list: ")
print(game_list)
print("\nHere is the reversed sorted list: ")
print(sorted(game_list, reverse=True))
print("\nHere is the original list again: ")
print(game_list)
print("\nReversing list: ")
game_list.reverse()
print(game_list)
print("\nReversing list again: ")
game_list.reverse()
print(game_list)
print("\nSorting the list in alphabetical order: ") 
game_list.sort()
print(game_list)
print("\nSorting list in alphabetical reversed order: ")
game_list.sort(reverse=True)
print(game_list)