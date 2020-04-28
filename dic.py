import os, sys, io
word = input("enter word:")

lookup = "diction.py " + word + ' -d'
exs = input("see all examples? press y. top example? press t:")
if exs == 'y':
	lookup = lookup + ' -e'
if exs == 't':
	lookup = lookup + ' -te'
rels = input("see related words?")
if rels == 'y':
	lookup = lookup + ' -r'
etys = input("see etymologies?")
if etys == 'y':
	lookup = lookup + ' -et'
freqs = input("see word frequency over time? Will open browser:")
if freqs == 'y':
	interval = input("Enter start year [SPACE] end year.")
	lookup = lookup + ' -f' + interval

results = lookup + " >" + " dicts/%s.txt" % word
os.system(results)
filename = "dicts/%s.txt" % word
"""with open(filename, 'w', encoding='utf-8') as f:

	f.write(str(results))
	

	f.close()"""
