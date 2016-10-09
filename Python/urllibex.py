import urllib
fhand=urllib.urlopen('http://www.py4inf.com/code/remo.txt')
for line in fhand:
    print line.strip()
 