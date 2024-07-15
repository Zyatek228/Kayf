a = [int(x) for x in open('17(3).txt')]
maxcolvstr = 0
k = 0
for i in range(len(a)):
    if a.count(a[i]) > maxcolvstr:
        maxcolvstr = a.count(a[i])
        moda = a[i]


for i in range(len(a)):
    if abs(a[i]-moda) <= 300:
        k+=1

print(moda, k)