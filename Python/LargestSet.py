import itertools
# Complete the function below.
#Program to find largest possible set of elements which sum is less then equalt to k.
#There are 3 inputs, no of elements in the set a_cnt, list of elements a and k.
a_cnt = 0
a_cnt = int(input())
a_i=0
a = []
while a_i < a_cnt:
    a_item = int(input())
    a.append(a_item)
    a_i+=1  
k = int(input());
a.sort()
x=list()
for L in range(0, len(a)+1):
    for subset in itertools.combinations(a, L):
        x.append(subset)
        #print(x)
x.pop(0)
#print(x)
L=0
y=0
for L in range(0,len(x)):
    if sum(x[L])<=k:
        if (y<=len(x[L])):
            y=len(x[L])
            print(sum(x[L]))
print("Largest Length",y)            