import re
file=raw_input("Enter file name:")
handle=open(file,"r")
d=dict()
e=dict()
for line in handle:
    x=re.findall('^From: ([^*\s]*)',line)
    if len(x)==0:continue
    d[x[0]]=d.get(x[0],0)+1
for k,v in d.items(): print k,v
handle=open(file,"r")
for mline in handle:
    x=re.findall('^From:.*@([^*\s]*)',mline)
    if len(x)==0:continue
    e[x[0]]=e.get(x[0],0)+1
for k,v in e.items(): print k,v
