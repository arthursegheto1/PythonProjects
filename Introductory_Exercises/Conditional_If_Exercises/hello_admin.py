users = ['admin','arthur', 'maria', 'gustavo', 'joao']

if users == []:
        print("We need to find some users!")

for user in users:
    if users == []:
        print("We need to find some users!")
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")