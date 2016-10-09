# Use words.txt as the file name
try:
    fname = raw_input("Enter file name: ")
    fh = open(fname)
    for line in fh:
        print(line.upper())
except:
    print("Wrong File Name")
