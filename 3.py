s = [int(x) for x in open('17(3).txt')]
res1 = 0
res2 = 0
tek = []

for i in range(len(s)-1):
    a = s[i]
    b = s[i+1]
    if a == b and tek.count(a) == 0:
        res1 += 2
        res2 = max(res2, a)
        tek.append(a)
    elif a == b and tek.count(a) > 0:
        res1 += 1
        res2 = max(res2, a)
        tek.append(a)
    elif a != b:
        tk = []

print(res1, res2)


