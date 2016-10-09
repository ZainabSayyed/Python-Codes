try:
    fname = raw_input("Enter file name: ")
	#if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
    count = 0
    l=0
    for line in fh:
        if line.startswith('X-DSPAM-Confidence: '):
            text = "X-DSPAM-Confidence:    0.8475"
            l=float(text[text.find('0'):text.find('0')+6])+l
            count=count+1
            print(l)
    print "There were", count, "lines in the file with From as the first word"
except:
    print("Invalid File")