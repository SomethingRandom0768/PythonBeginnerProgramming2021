
# I basically copied and pasted the function code from 8-7

def make_album(artist_name, album_title, number_songs=None):
    album = {'Artist Name': artist_name,
             'Album Title': album_title,
             }
    if number_songs:
        album['Number of Songs'] =  number_songs
    return album

while True:
    artist_name = input("What's the name of the artist? (Press 'q' to exit) ")
    if artist_name == 'q':
        break
    album_title = input("What's the name of their album?")

    answer = input("Would you like to enter the amount of songs the album has? (yes/no) ")

    if answer == 'yes':
        number_of_songs = input("How many songs are in the album?")
        print( make_album(artist_name, album_title, number_of_songs) )
    else:
        print( make_album(artist_name, album_title) )

