set lookupvar = %cd%
set %lookupvar %/wiki.py=wiki
set %lookupvar %/l.py=l
set %lookupvar %/dic.py=dic
python diction.py
chdir %HOMEPATH%
notepad "diction.ini"
cd %lookupvar %