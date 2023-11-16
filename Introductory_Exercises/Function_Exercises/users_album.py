# Here I will use the code of "album.py" exercise.
# In this version of the code, I'll use a "while" loop to allow users to enter
# an album's artist and title.

def make_album(artist_name, album_title):
    """Return a music album information provided by the user"""
    album = f"{artist_name} {album_title}"
    return  album.title()

while True:
    print("\nPlease enter the name of your favorite artist and your favorite album:")
    print("(enter 'q' at any time to quit)")

    art_name = input("Artist name: ")
    if art_name == 'q':
        break
    
    album_name = input("Album name: ")
    if album_name =='q':
        break

    print(f"\nYour favorite artist and album are: {art_name.title()}, {album_name.title()}!")