#Shortest possible substring contains all alphabets present in string
def short_string(s):
    print len(s)
    substring=[]
    dict={}
    for i in range(len(s)):
        if dict.get(s[i])==None:
            dict[s[i]]=dict.get(s[i],0)+1
        for j in range(i+1,len(s)+1):
            substring.append(s[i:j])
    min_substr=len(dict)
    print ('min_length',min_substr,dict)
    unique_char=[]
    substr=[]
    for key,value in dict.items():
        unique_char.append(key)
    print unique_char
    for i in substring:
        if len(i)>=min_substr:
            if set(unique_char)<=set(i):
                substr.append(i)
    substr=sorted(substr,key=lambda i:len(i))   
    print substr
    return(substr)

if __name__=='__main__':
    mylist=[]
    string=raw_input("Enter String")
    mylist=short_string(string)
    print mylist[0]
