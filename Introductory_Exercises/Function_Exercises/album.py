# Here I should write a function that builds a dictionary
# describing a music album.
# The function should take in an artist name and an album title, and it should
# return a dictionary containing these 2 pieces of information.

def make_album(artist_name, album_title, number_songs=None):
    """Return a music album information"""
    album = {'artist': artist_name, 'title': album_title}
    if number_songs:
        album['number_songs'] = number_songs
    return album

# Printing each return value to show that the dictionary is storing 
# the album information correctly
musician = make_album ('shawn mendes', 'wonder', number_songs='14')
print(musician)

musician = make_album ('jvke', 'this is what ____ feels like (Vol. 1-4)', number_songs='12')
print(musician)

musician = make_album ('imagine dragons', 'evolve')
print(musician)
