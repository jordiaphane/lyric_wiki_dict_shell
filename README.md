Simple little dictionary, wikipedia, and wordnik lookup straight from cmd line

Using the commands 'dic' for dictionary, 'l' for lyrics, and 'wiki' for wikipedia, this tool gives you easy, storable txt files of lyrics, defnitions(and much more syntax and semantics), and wikipedia entries.

Once you have everything set up, you can move the python files to a more convenient directory and use them from there, or add them to your PATH.

YOU WILL NEED TWO API KEYS:

  1) from genius.com, for the lyrics.

    Go to the site,
    http://genius.com/api-clients


    and just follow the instructions. you don't need a valid reason to receive an API code. 
    You can say whatever you want and you will still receive one.

Once you get your API code, open 'l.py' in any text editor and enter your key in between the quotes in line 8, where it says "YOURKEYHERE".


  2) The next one, for the dictionary, you will need to get at:

    http://developer.wordnik.com
    by doing the same process, more or less.

====installation=====
in the shell of your choosing:

  git clone https://github.com/jordiaphane/lyric_wiki_dict_shell.git

  cd lyrics_wiki_dict_shell

  pip install -r requirements.txt

  source[for mac] sh[for win/lin] env.sh
  this should open a long congifuration file, but where you enter the API key for the dictionary is the second line. WITH NO QUOTATIONS   ENTER YOUR WORDNIK KEY, mentioned in line 22 of this README. 
  There will be a screenshot in 'examples' folder showing where to add the key

  CLOSE OUT OF THE CONFIGURATION FILE, SAVE.

  HIT ENTER IN SHELL


from here, you should be done!

all lyrics, wiki entries, and dict entries are saved as text files named after their search terms. very small text files, so no need to worry about size.

I've been using this tool for so long thought I'd share!
