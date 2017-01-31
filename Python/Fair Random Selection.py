import random
def main():
    dict={'banana':100000,'mango':75000,'apple':50000}
    n=1
    list=[]
    count=0
    while n==1:
        i=random.random()
        if i<=0.5 and 'apple' not in list:
            print 'apple:',dict.get('apple')
            list.append('apple')
            count=count+1
        if i>0.5 and i<=0.75 and 'mango' not in list:
            print 'mango:',dict.get('mango')
            list.append('mango')
            count=count+1
        if i>0.75 and i<=1 and 'banana' not in list:
            print 'banana:',dict.get('banana')
            list.append('banana')
            count=count+1
        if count==3:
            count=0
            list.remove('apple')
            list.remove('banana')
            list.remove('mango')
        n=int(raw_input("n:"))
        
if __name__ == "__main__":
    main()
