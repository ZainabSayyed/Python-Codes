def Odd_Position(string):
    print "Odd Position"
    for i in range(1,len(string))[::2]:
        print string[i]
    
def Even_Position(string):
    print "Even Position"
    for i in range(0,len(string))[::2]:
        print string[i]
        
if __name__=="__main__":
    string=raw_input("Enter string to be split")
    Odd_Position(string)
    Even_Position(string)
