import os, sys
import re
os.system("source env.sh")
os.mkdir('wikis')
ww = input('wiki:')

wpage = wikipedia.page(ww)
sums = wikipedia.summary(ww)
print(sums)

filename = "wikis/%s.txt" % ww
with open(filename, 'w', encoding='utf-8') as f:
	
	yn = input('include full page? y/n')
	if yn == 'y':
		content = wpage.content
		f.write(sums + '\n' + content)
	f.write(sums)
	

	f.close()
