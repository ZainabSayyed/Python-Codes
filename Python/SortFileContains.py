fname = raw_input("Enter file name: ")
lst=[]
try:
    with open(fname, 'r') as fh:
        for line in fh:
            dummy=line.split()
            n=len(dummy)
            for i in xrange(0,n):
                lst.append(dummy[i])
            i=0
    lst.sort()
    print (lst)
except:
    print("Invalid file")
        