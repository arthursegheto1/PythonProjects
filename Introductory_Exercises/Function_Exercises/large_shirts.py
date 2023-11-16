# I'll modify the 't_shirt.py'
# The T-Shirts now will be large by default with a message 
# that reads 'I love Python' 

def make_shirt(size='L', text='I love Python'):
    print(f"The size of the shirt is {size} and the text is {text}")

# Default shirt
make_shirt()   

# Medium shirt with default text
make_shirt(size='M')

# Any shirt size with a different text
make_shirt(size='S', text='Good vibes only')