import itertools
# Complete the function below.
_a_cnt = 0
_a_cnt = int(raw_input())
_a_i=0
_a = []
while _a_i < _a_cnt:
    _a_item = int(raw_input());
    _a.append(_a_item)
    _a_i+=1  
k = int(raw_input());
_a.sort()
x=[]
for L in range(0, len(_a)+1):
    for subset in itertools.combinations(_a, L):
        x.append(subset)
        print(x)
x.remove(0)
L=0
y=0
for L in range(0, len(x)+1):
    if sum(x[L])<=k:
        if (y <=len(x[L])+1):
            y=len(x[L])
            print(sum(x[L])
#print("Largest Length",y)