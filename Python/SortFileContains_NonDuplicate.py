fname = raw_input("Enter file name:")
lst=[]
try:
    with open(fname, 'r') as fh:
        for line in fh:
            dummy=line.split()
            for i in dummy:
                if(i not in lst):
                    lst.append(i)
    lst.sort()
    print (lst)
except:
    print("Invalid file")