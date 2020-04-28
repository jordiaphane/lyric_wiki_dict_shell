Simple little dictionary, wikipedia, and wordnik lookup straight from cmd line

Using the commands 'dic' for dictionary, 'l' for lyrics, and 'wiki' for wikipedia, this tool gives you easy, saveable, extensive access to frameworks available through their APIs:

for the dictionary:
sign up for https://developer.wordnik.com/ and request an API

for the lyrics:
http://genius.com/api-clients

you WILL need these API keys, and the setup guides you through entering them into the code. For Lyrics, simply open 'l.py' in any text editor and enter your key in between the quotes in line 8.

====installation=====

pip install -r requirements.txt
source[for mac] sh[for win/lin] env.sh
this should open a long congifuration file, but where you enter the API key for the dictionary is the second line. WITH NO QUOTATIONS ENTER YOUR KEY


from here, you should be done!

all lyrics, wiki entries, and dict entries are saved as text files named after their search terms. very small text files, so no need to worry about size.

I've been using this tool for so long thought I'd share!