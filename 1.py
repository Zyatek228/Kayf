s = [int(x) for x in open('17(1).txt')]
otv = []

for i in range(0, len(s)-4, 5):
    oc = []
    oc.append(s[i])
    oc.append(s[i+1])
    oc.append(s[i+2])
    oc.append(s[i+3])
    oc.append(s[i+4])
    sr = sum(oc)/len(oc)
    print(sr)
    if sr <= 3.44:
        otv.append(sr)

print(len(otv), min(otv))