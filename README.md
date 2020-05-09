Simple little dictionary, wikipedia, and wordnik lookup straight from cmd line

Using the commands 'dic' for dictionary, 'l' for lyrics, and 'wiki' for wikipedia, this tool gives you easy, storable txt files of lyrics, defnitions(and much more syntax and semantics), and wikipedia entries.

Once you have everything set up, you can move the python files to a more convenient directory and use them from there, or add them to your PATH.

1) Lyrics

Searching artist and song will print lyrics to prompt, if found. If not, returns a list of possible sugggestions. Usually makes up for typos. After printed to command prompt and saved as a plain text document in the 'L' folder, another prompt will ask if you would like to pull up results for the song on youtube music, opening your browser with the song already queried.

2) Wikipedia

Searching with wiki is less forigiving with typos, but makes decent assumptions about what it is you're looking for. Prints the summary to the shell, then asks if you'd like to see the full wikipedia entry. If yes, that is saved into the 'WIKI' folder . 

3) Dictionary(via Wordnik)

Wordnik is my favorite dictionary on the internet becuase it aggregates official and unofficial dictionaries alike, uses its own APIs to draw examples from books, newspapers, and articles, and provides simple entymological information as well as word usage over time. The only problem with it is searching for lexemes. For example, searching for bears will give you no information other than "plural for bear". Stick to singular nouns and the simplest form of the word you are looking for in general.

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
    
    this should open a long congifuration file, but where you enter the API key for the dictionary is the second line. 
    WITH NO QUOTATIONS, enter the wordnik key, with no spaces after the '='
    mentioned in line 22 of this README is where to acquire this key. 
    There will be a screenshot in 'examples' folder showing where to add the key

    CLOSE OUT OF THE CONFIGURATION FILE, SAVE.

    HIT ENTER IN SHELL


from here, you should be done!

====USAGE====

      l/wiki/dic[enter]
      follow instructions
      hit lowercase 'y' for yes, any other key for no(unless otherwise specified)
      

all lyrics, wiki entries, and dict entries are saved as text files named after their search terms. very small text files, so no need to worry about size.



I've been using this tool for so long thought I'd share!