m=[12,22,11,42,56,78,98,90]
i=0
while i<len(m)-1:
    j=0
    min=i
    while j<len(m):
        if m[min]<m[j]:
            min=j
        m[i],m[min]=m[min],m[i]
        j+=1
    i+=1
print(m)