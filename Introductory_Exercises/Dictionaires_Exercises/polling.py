favorite_languages = {
    'arthur': 'python',
    'maria': 'java',
    'gustavo': 'java',
    'pedro': 'c',
}
names = ['arthur', 'maria', 'joão', 'matheus']
for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"You should take our poll, {name.title()}!")