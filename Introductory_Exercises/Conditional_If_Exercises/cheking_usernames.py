current_users = ['arthur', 'maria', 'gustavo', 'joao', 'felipe']
new_users = ['ARTHUR', 'pedro', 'matheus', 'maria', 'jordana']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username '{new_user}' already in use, please choose another one.")
    else:
        print(f"Username '{new_user}' available.")