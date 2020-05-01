import sys, os, io
import lyricsgenius
artistname = input('artist:')
songtitle = input('song:')
geniusgenius = lyricsgenius.Genius("YOURAPIHERE")   

song = geniusgenius.search_song(


songtitle,
artistname) 
songlyrics = song.lyrics
print(song.lyrics)


filename = "L/%s_%s.txt" % (artistname, songtitle)
with open(filename, 'w') as f:
	f.write(songlyrics)
	f.close()

