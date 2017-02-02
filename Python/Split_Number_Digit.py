def split_number(number):
    digit=[]
    string=str(number)
    digit=map(int,string)
    return(digit)

if __name__=="__main__":
    number=int(raw_input("Enter number to be split"))
    print split_number(number)
