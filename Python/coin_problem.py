#coin problem
n=11
a=[2,4,5,7,3]
a.sort(reverse = True)
coin_combination=[]
for i in range(0,len(a)-1):
    counter=dict()
    remainder= n % a[i]
    quotient = n/a[i]
    counter[a[i]]=quotient
    if remainder != 0:
        for j in range(i,len(a)-1):
            remainder1 = remainder %a[j]
            quotient1 = remainder /a[j]
            counter[remainder]=quotient1
            if remainder1 == 0:
                break
    total,number_of_coin = 0 , 0
    for k,v in counter.items():
        total = total + k*v
        number_of_coin = number_of_coin +v
        if total == n:
            counter["number_of_coin"]= number_of_coin
            coin_combination.append(counter)
print coin_combination