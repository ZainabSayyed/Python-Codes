x=int(input ("Enter No"))
if ((0<=x) and (x<=15)):
    y=[0]
    z=0
    if(x>1):
        y.append(1)
        for i in range(0,x-2):
            z=y[i]+y[i+1]
            y.append(z)
    else:
        if(x==0):
            y.remove(0)
    if(x>1):    
        for i in range (0,x):
            y[i]=y[i]**3
    
    print(y)
else:print('Sorry Enter valid Number')
