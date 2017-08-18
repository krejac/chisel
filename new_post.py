#encoding: utf-8
import urllib, time, os

# Ask for post title
title = raw_input("What do you want title to say? \n> ")

# urlencode title
slug = urllib.quote(title.replace(' ', '-')).lower()

# set date
ENTRY_TIME_FORMAT = "%d-%m-%Y" # from chisel.py
date = time.strftime(ENTRY_TIME_FORMAT)

# write filename
file = 'posts/' + slug + '.md'
with open(file,'w') as f:
    f.write(title + '\n' + date + '\n\n\n' +
    "**[TL;DR](http://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn't_read)** - ")

# open file
os.system("atom " + file)
