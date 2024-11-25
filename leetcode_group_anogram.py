a = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = []
used = [] 

for i in range(len(a)):
    if a[i] in used:
        continue  
    c = []  
    for j in range(len(a)):
        if sorted(a[i]) == sorted(a[j]):
            c.append(a[j])
            used.append(a[j])  
    d.append(c)  

print(d)