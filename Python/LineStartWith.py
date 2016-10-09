# Use the file name mbox-short.txt as the file name
try:
    fname = raw_input("Enter file name: ")
    count=0
    total=0
    fh = open(fname)
    with open(fname, 'r') as fh:
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:") : continue
            count=count+1
            x=float(line[line.find('0'):line.find('0')+6])
            total=total+x
        average=float(total)/count
    print('Average spam confidence: '+str(average))
except:
    print('Sorry Invlaid File Name')