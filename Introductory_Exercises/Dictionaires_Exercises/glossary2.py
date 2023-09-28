words = {
    'for' : 'loops through a list',
    'if' : 'conditional statement',    
    'print' : 'print a message',
    'list' : 'list of items',
    'dictionary' : 'collection of key-value pairs',
    'tuple' : 'immutable list',
    'set' : 'unique list',
    'variable' : 'placeholder for a value',
    'string' : 'a series of characters',
    'integer' : 'a whole number',
}

for word, meaning in words.items():
    print(f"\nWord: {word.title()}")
    print(f"Meaning: {meaning}")