import sys, os, io
import lyricsgenius
import re
import webbrowser
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

print("\n")
yt = input('search on youtube?:')
if yt == 'y':
	songtitle1 = re.sub("[ ]","+", songtitle)
	artistname1 = re.sub("[ ]","+", artistname)
	url = "https://music.youtube.com/search?q=" + artistname1 + "+" + songtitle1
	print(url)
	webbrowser.open(url)