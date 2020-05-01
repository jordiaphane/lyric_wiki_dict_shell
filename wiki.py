import os, sys, io
import wikipedia
import re

ww = input('wiki:')

wpage = wikipedia.page(ww)
sums = wikipedia.summary(ww)
print(sums)

filename = "WIKI/%s.txt" % ww
with open(filename, 'w', encoding='utf-8') as f:
	
	yn = input('include full page?(y/n)')
	if yn == 'y':
		content = wpage.content
		print(content)
		f.write(sums + '\n' + content)
	f.write(sums)
	

	f.close()
