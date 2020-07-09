import sys, os, io, re
import lyricsgenius
import webbrowser
artistname = input('artist:')
songtitle = input('song:')
geniusgenius = lyricsgenius.Genius("YOURAPIHERE")   

song = geniusgenius.search_song(



songtitle
, artistname) 
songlyrics = song.lyrics
print(song.lyrics)


filename = "C:/Users/jornado/AS/DATA/L/%s_%s.txt" % (artistname, songtitle)
with open(filename, 'w') as f:
	f.write(songlyrics)
	f.close()

songsearch = input('search on youtube?')

if songsearch == 'y':
	plusartist = str(re.sub(' ', '+', artistname))
	plussong = str(re.sub(' ', '+', songtitle))
	url = 'https://music.youtube.com/search?q=' + plusartist + ' ' + plussong
	webbrowser.open(url)
"""### to use this
you need to download and install ffmpeg from: https://ffmpeg.org/
lets say you install it to c:/ProgramData/ffmpeg, you then need to add that bin to your system PATH"""
download = input('download? y/n')
if download == 'y':
	oorl = input('copy url here')

	os.chdir('L')
	os.mkdir('dls')

	os.system('youtube-dl -x --audio-format mp3 ' + oorl)
