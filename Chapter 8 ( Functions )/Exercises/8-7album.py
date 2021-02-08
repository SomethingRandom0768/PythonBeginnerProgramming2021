

def make_album(artist_name, album_title, number_songs=None):
    album = {'Artist Name': artist_name,
             'Album Title': album_title,
             }
    if number_songs:
        album['Number of Songs'] =  number_songs
    return album

# I don't know music that much :(

print(make_album('Frank Sinatra','Come Fly With Me', 15))

print(make_album('The Ink Spots', 'Volume One'))
