import sys, os, io
import lyricsgenius
os.system("source env.sh")
os.mkdir('lyrics')
artistname = input('artist:')
songtitle = input('song:')
try:
	geniusgenius = lyricsgenius.Genius("")   
except:
	print("get a genius code, then open this file and add it to line 6 in the empty quotes")
song = geniusgenius.search_song(



artistname
, songtitle) 
songlyrics = song.lyrics
print(song.lyrics)


filename = "lyrics/%s_%s.txt" % (artistname, songtitle)
with open(filename, 'w') as f:
	f.write(songlyrics)
	f.close()

